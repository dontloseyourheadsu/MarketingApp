# Marketing app

Simple marketing app to showcase products and services through images or videos that connect to third-party ad services.

## Functional Requirements

- CRUD images
- CRUD videos
- CRUD ads
- CRUD subscribed emails
- CRUD Organizations
- Group emails
- Send selected ads to emails with scheduling options

(Future: Publish/unpublish google ads)

## Non-Functional Requirements

- Performance: The app should load and respond quickly to user interactions.
- Scalability: The app should be able to handle a growing number of users and data.
- Security: User data, especially email addresses, must be stored securely and comply with data protection regulations.
- Usability: The app should have an intuitive interface for both marketing users and administrators.

## Tech Stack

- Frontend: Angular
- Backend: Axum
- Database: PostgreSQL
- Authentication: JWT, OAuth
- Cloud Storage: AWS S3