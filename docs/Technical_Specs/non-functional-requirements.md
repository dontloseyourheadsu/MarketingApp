# 📈 Non-Functional Requirements

## High Consistency

- Use a strong consistency database (e.g., PostgreSQL)
- Eventual consistency okay for analytics, but not for ad content

## High Idempotency

- API endpoints must support idempotency keys (especially `POST /ads/{id}/send`)
- Avoid duplicate sends or uploads

## Availability & Low Latency

- Use CDN for media
- Async background jobs for email sending
- Caching for static lists
