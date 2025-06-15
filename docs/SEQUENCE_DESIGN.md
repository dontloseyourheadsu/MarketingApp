# Sequence Diagrams for Key Flows

## 1. User Authentication (login → JWT → refresh)

![Login Flow](images/login_flow.png)

```plantuml
@startuml Login_Flow
actor User
participant FE          as "Web / Mobile Frontend"
participant APIG        as "Public API Gateway"
participant AUTH        as "Auth Service"
database  PG            as "PostgreSQL"

User  -> FE       : enter credentials / OAuth callback
FE    -> APIG     : POST /auth/login  (JSON creds or OAuth code)
APIG  -> AUTH     : validate credentials
AUTH  -> PG       : SELECT user, verify password
PG    --> AUTH
AUTH  --> APIG    : 200 OK\naccess token (JWT) + refresh token
APIG  --> FE      : tokens

== subsequent requests ==
User  -> FE       : normal API call
FE    -> APIG     : Authorization: Bearer <JWT>

== token expiry ==
FE    -> APIG     : POST /auth/refresh with refresh token
APIG  -> AUTH
AUTH  -> PG       : check refresh token, rotate if needed
AUTH --> APIG     : new JWT
APIG --> FE
@enduml
```

---

## 2. Media Upload (via pre-signed S3 URL)

![Media Upload Flow](images/media_upload_flow.png)

```plantuml
@startuml Media_Upload
' -----------------------------------------------------------
' Participants (no database/cloud keywords in sequence diagrams)
' -----------------------------------------------------------
actor MarketingUser as MU
participant FE           as "Web / Mobile Front-end"
participant APIG         as "Public API Gateway"
participant MEDIA_SVC    as "Media Service"
participant PG           as "PostgreSQL"
participant S3           as "Amazon S3"
participant CF           as "CloudFront CDN"

' -----------------------------------------------------------
' 1. User chooses a file
' -----------------------------------------------------------
MU  -> FE            : choose image / video

' -----------------------------------------------------------
' 2. Create placeholder + get pre-signed URL
' -----------------------------------------------------------
FE  -> APIG          : POST /media  {filename, size, type}
APIG -> MEDIA_SVC    : createAsset(metadata)
MEDIA_SVC -> PG      : INSERT asset stub (status=PENDING)
PG  --> MEDIA_SVC

note right of MEDIA_SVC
Generate pre-signed PUT URL  
(expiry = 15 min)
end note

MEDIA_SVC --> APIG   : 201 Created\n{asset_id, presigned_url}
APIG --> FE          : returns asset_id + presigned_url

' -----------------------------------------------------------
' 3. Client uploads directly to S3
' -----------------------------------------------------------
FE  -> S3            : HTTP PUT <presigned_url>  (binary)
S3 --> FE            : 200 OK

' -----------------------------------------------------------
' 4. Notify backend that upload is complete
' -----------------------------------------------------------
FE  -> APIG          : POST /media/{asset_id}/complete
APIG -> MEDIA_SVC    : markUploaded(asset_id)
MEDIA_SVC -> PG      : UPDATE asset SET status=READY, path=...
PG  --> MEDIA_SVC

MEDIA_SVC -> CF      : (optional) Invalidate path
MEDIA_SVC --> APIG   : 200 OK
APIG --> FE          : upload confirmed
@enduml
```
---

## 3. Schedule & Send Email Campaign

![Email Campaign Flow](images/email_campaign_flow.png)

```plantuml
@startuml Email_Campaign
actor MarketingUser as MU
participant FE
participant APIG
participant EMAIL_SVC
participant SCHED_SVC
participant QUEUE_SQS       as "SQS Job Queue"
participant EmailWorker     as "EMAIL_SVC Worker"
participant ESP             as "SES / SendGrid"
participant ANALYTICS_SVC

' -----------------------------------------------------------
' 1. Schedule Campaign
' -----------------------------------------------------------
MU  -> FE              : Fill campaign form
FE  -> APIG            : POST /emails {template, group, time}
APIG -> EMAIL_SVC      : create draft
EMAIL_SVC --> APIG     : 201 Created (campaign_id)

' -----------------------------------------------------------
' 2. Scheduling
' -----------------------------------------------------------
APIG -> SCHED_SVC      : POST /schedule (campaign_id, datetime)
SCHED_SVC --> APIG     : 202 Accepted

' -----------------------------------------------------------
' 3. Scheduler pushes job
' -----------------------------------------------------------
SCHED_SVC -> QUEUE_SQS : push due job (campaign_id)

' -----------------------------------------------------------
' 4. Worker handles job
' -----------------------------------------------------------
QUEUE_SQS --> EmailWorker     : pull job
EmailWorker -> EMAIL_SVC      : fetch campaign + recipients
EmailWorker -> ESP            : send batch
ESP --> EmailWorker           : delivery status
EmailWorker -> ANALYTICS_SVC  : emit send events
@enduml
```

---

## 4. Subscriber Unsubscribe (global & group-level)

![Unsubscribe Flow](images/unsubscribe_flow.png)

```plantuml
@startuml Unsubscribe_Flow
actor Subscriber
participant EmailClient     as "Mail Client"
participant FE              as "Preference Centre"
participant APIG
participant UNSUB_SVC       as "Unsubscribe Service"
participant PG              as "PostgreSQL"
participant EMAIL_SVC       as "Email Campaign Service"
participant ESP             as "SES / SendGrid"

' -----------------------------------------------------------
' 1. User clicks email unsubscribe link
' -----------------------------------------------------------
Subscriber -> EmailClient : click unsubscribe link (JWT)
EmailClient -> FE         : open /emails/unsubscribe?token=...
FE -> APIG                : GET /preferences (JWT)
APIG -> UNSUB_SVC         : validate token, lookup subscriber
UNSUB_SVC -> PG           : SELECT subscription preferences
PG --> UNSUB_SVC
UNSUB_SVC --> APIG        : 200 OK + current prefs
APIG --> FE               : render preference centre

' -----------------------------------------------------------
' 2. User submits unsubscribe
' -----------------------------------------------------------
Subscriber -> FE          : click "Unsubscribe"
FE -> APIG                : POST /emails/unsubscribe {global=true}
APIG -> UNSUB_SVC         : request unsubscribe
UNSUB_SVC -> PG           : UPDATE subscribers SET global_opt_out=true
UNSUB_SVC -> EMAIL_SVC    : publish preference-updated event
UNSUB_SVC --> APIG        : 204 No Content
APIG --> FE               : success screen

' -----------------------------------------------------------
' 3. Confirmation email (optional)
' -----------------------------------------------------------
UNSUB_SVC -> ESP          : send confirmation email
ESP --> UNSUB_SVC         : 202 Accepted
@enduml
```