# ⏰ Scheduling Engine

## Job Structure

```json
{
  "id": "job-uuid",
  "type": "email-campaign",
  "status": "scheduled",
  "data": {
    "ad_id": "ad-uuid",
    "email_group_id": "group-uuid",
    "template_id": "template-uuid"
  },
  "schedule": {
    "start_time": "2025-06-20T15:00:00Z",
    "timeout": 3600,
    "retry_policy": {
      "max_retries": 3,
      "backoff_factor": 1.5
    }
  },
  "created_by": "user-uuid",
  "created_at": "2025-06-13T10:30:00Z"
}
```

## Scheduling Flow

1. Marketing user creates scheduled job through API
2. Scheduler service validates job parameters and stores job
3. Cron service checks for due jobs every minute
4. Due jobs pushed to job queue for processing
5. Worker pulls job and executes task
6. Results stored and notifications sent

## Reliability Features

- At-least-once delivery semantics
- Automatic retries with exponential backoff
- Dead letter queue for failed jobs
- Idempotency keys to prevent duplicate execution
- Job timeout monitoring

## Monitoring & Management

- Job status dashboard
- Failure alerts and notifications
- Manual intervention capabilities (cancel, reschedule, force-run)
- Historical execution logs with filtering
- Performance metrics collection
