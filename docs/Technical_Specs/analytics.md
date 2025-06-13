# 📊 Analytics

## Analytics Data Model

```plantuml
@startuml
entity "AnalyticsEvent" {
  * id : UUID
  --
  event_type : ENUM('email_open','email_click','ad_view','ad_click')
  timestamp : TIMESTAMP
  user_agent : TEXT
  ip_address : VARCHAR
  geolocation : JSONB

  # Related Entities
  ad_id : UUID (nullable)
  email_id : UUID (nullable)
  subscriber_id : UUID (nullable)
  campaign_id : UUID (nullable)

  # Custom Properties
  properties : JSONB
}

entity "AnalyticsAggregate" {
  * id : UUID
  --
  entity_type : ENUM('ad','email','campaign')
  entity_id : UUID
  time_period : ENUM('hour','day','week','month')
  period_start : TIMESTAMP
  metrics : JSONB
}
@enduml
```

## Storage Strategy

- Time-series database for raw events
- Periodic aggregation to pre-computed summaries
- Hot storage (30 days) → Warm storage (90 days) → Cold storage (archival)

## Event Collection

- Email opens
- Ad interactions
- Deliveries and bounces (not delivered)
- UTM (Urchin Tracking Module) parameter tracking for attribution

## Analytics API Endpoints

- `GET /analytics/ads/{id}` (Ad performance metrics)
- `GET /analytics/campaigns/{id}` (Campaign performance)
- `GET /analytics/email-groups/{id}/performance` (Group engagement)
- `GET /analytics/dashboard` (Aggregate metrics for dashboards)

## Data Retention

- Raw events: 90 days
- Hourly aggregates: 12 months
- Daily aggregates: 36 months
- Monthly aggregates: indefinite
