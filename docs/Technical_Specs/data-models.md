# 🧩 Data Models

## Simplified Data Models

```plaintext
User { id, name, email, role, team_id }
Team { id, name, description }
Media { id, type: image|video, url, metadata, uploaded_by, created_at }
Ad { id, title, description, media_ids[], status, created_by, team_id }
EmailSubscriber { id, email, group_id, subscribed_at }
EmailGroup { id, name, description }
AdSendEvent { id, ad_id, email_group_id, sent_by, status, sent_at }
```

## SQL UML Diagram (PostgreSQL)

![SQL UML Diagram](images/sql_uml_diagram.png)

```plantuml
@startuml
entity "User" as User {
  * id : UUID
  --
  name : VARCHAR
  email : VARCHAR
  role : ENUM('marketing','consumer')
  team_id : UUID
}

entity "Team" as Team {
  * id : UUID
  --
  name : VARCHAR
  description : TEXT
}

entity "Media" as Media {
  * id : UUID
  --
  type : ENUM('image','video')
  url : VARCHAR
  metadata : JSONB
  uploaded_by : UUID
  created_at : TIMESTAMP
}

entity "Ad" as Ad {
  * id : UUID
  --
  title : VARCHAR
  description : TEXT
  status : ENUM('draft','scheduled','published')
  created_by : UUID
  team_id : UUID
}

entity "AdMedia" as AdMedia {
  * ad_id : UUID
  * media_id : UUID
}

entity "EmailGroup" as EmailGroup {
  * id : UUID
  --
  name : VARCHAR
  description : TEXT
}

entity "EmailSubscriber" as EmailSubscriber {
  * id : UUID
  --
  email : VARCHAR
  group_id : UUID
  subscribed_at : TIMESTAMP
  global_opt_out : BOOLEAN
  unsubscribed_groups : UUID[]
  last_updated : TIMESTAMP
}

entity "AdSendEvent" as AdSendEvent {
  * id : UUID
  --
  ad_id : UUID
  email_group_id : UUID
  sent_by : UUID
  status : ENUM('pending','sent','failed')
  sent_at : TIMESTAMP
}

Team ||--o{ User : has
Team ||--o{ Ad : owns
User ||--o{ Media : uploads
User ||--o{ Ad : creates
Ad ||--o{ AdMedia : links
Media ||--o{ AdMedia : linked_to
EmailGroup ||--o{ EmailSubscriber : contains
Ad ||--o{ AdSendEvent : logs
EmailGroup ||--o{ AdSendEvent : targeted_by
User ||--o{ AdSendEvent : triggers
@enduml
```

## NoSQL Document Schemas (MongoDB)

![NoSQL Document Schemas](images/nosql_document_schemas.png)

```plantuml
@startuml
skinparam classAttributeIconSize 0

class User << (D,#FFAAAA) document >> {
   + _id : ObjectId
   + name : string
   + email : string
   + role : string    // 'marketing' or 'consumer'
   + team_id : ObjectId
}

class Team << (D,#FFAAAA) document >> {
   + _id : ObjectId
   + name : string
   + description : string
   + member_ids : List<ObjectId>
}

class Media << (D,#FFAAAA) document >> {
   + _id : ObjectId
   + type : string       // 'image' or 'video'
   + url : string
   + metadata : object
   + uploaded_by : ObjectId
   + created_at : date
}

class Ad << (D,#FFAAAA) document >> {
   + _id : ObjectId
   + title : string
   + description : string
   + media_ids : List<ObjectId>
   + status : string     // 'draft','scheduled','published'
   + created_by : ObjectId
   + team_id : ObjectId
}

class EmailGroup << (D,#FFAAAA) document >> {
   + _id : ObjectId
   + name : string
   + description : string
}

class EmailSubscriber << (D,#FFAAAA) document >> {
   + _id : ObjectId
   + email : string
   + group_id : ObjectId
   + subscribed_at : date
}

class AdSendEvent << (D,#FFAAAA) document >> {
   + _id : ObjectId
   + ad_id : ObjectId
   + email_group_id : ObjectId
   + sent_by : ObjectId
   + status : string    // 'pending','sent','failed'
   + sent_at : date
}
@enduml
```
