# Functional Requirements

## 1. **CRUD for Media Content**

### Images & Videos

- Upload (store securely, validate format/size)
- View/List (with pagination, filters)
- Update (replace metadata or file)
- Delete (soft delete preferred)

## 2. **CRUD for Ads**

- Create Ad (title, description, media associations, call-to-action, tags)
- Read/List Ads (filter by campaign, status, media type, etc.)
- Update Ad content and media
- Delete Ad (soft delete for audit)

## 3. **CRUD for Subscribed Emails**

- Add email (with validation & duplication checks)
- View/List emails
- Group emails (custom named segments)
- Remove email / Delete groups

## 4. **Send Ads to Emails**

- Select Ads & Target Email Groups
- Compose custom message or template
- Send now or schedule
- Email sending via transactional email service (e.g., SendGrid, SES)
- Delivery tracking, open/click analytics

## 5. **User and Role Management**

### Roles: `marketing`, `consumer`

- Marketing:

  - Full access to ad and media management
  - Manage email groups
  - Send ads via email

- Consumer:

  - View-only access to published ads/content

## 6. **Marketing Teams**

- Teams contain users with marketing roles
- CRUD Teams (name, description, members)
- Team-level access to content

---

## 🚀 [Future] Google Ads Publishing

- Integration with Google Ads API

  - OAuth2 for account authorization
  - Create/update campaigns
  - Publish/unpublish ads

- Permission checks (only team admins or approved users)
- Audit log for external publishing actions

## 🧪 Audit & Security Considerations

- Audit logs: Ad creations, email sends, user changes
- Rate limits and abuse prevention
- Role-based access control (RBAC)
- Email opt-in/opt-out compliance
