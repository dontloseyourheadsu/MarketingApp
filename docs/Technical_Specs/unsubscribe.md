# Unsubscribe Management

## Unsubscribe API Endpoints

- `POST /emails/unsubscribe` (Global opt-out)
- `POST /email-groups/{group_id}/unsubscribe` (Group-specific opt-out)
- `GET /emails/{email}/preferences` (View current subscription status)
- `PUT /emails/{email}/preferences` (Update subscription preferences)

## Unsubscribe Flow

1. Every marketing email includes:
   - Group-specific unsubscribe link with encoded JWT
   - Global unsubscribe link with encoded JWT
2. Clicking either link directs to preference center or direct unsubscribe
3. Unsubscribe action updates database subscription status
4. Confirmation email sent for unsubscribe actions

## Preference Management

- User-facing preference center for managing subscriptions
- API respects preferences during audience selection
- Export of unsubscribed emails for external system synchronization
- Re-subscribe restrictions (require explicit opt-in)

## Compliance Features

- List-Unsubscribe email headers
- Unsubscribe link position (footer)
- Audit logs for all subscription changes
- Time-stamping of preference changes
- GDPR-compliant consent tracking
