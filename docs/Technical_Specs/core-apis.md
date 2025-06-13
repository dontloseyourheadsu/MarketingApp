# 🌐 Core APIs

## Media

- `POST /media` (Upload)
- `GET /media?type=image` (List)
- `DELETE /media/{id}`

## Ads

- `POST /ads`
- `GET /ads`
- `PUT /ads/{id}`
- `DELETE /ads/{id}`

## Emails

- `POST /emails`
- `GET /emails`
- `POST /email-groups`
- `GET /email-groups`
- `POST /ads/{id}/send` (Send ad to email group)

## Teams & Users

- `POST /teams`
- `GET /teams`
- `POST /users` (with role & team)
