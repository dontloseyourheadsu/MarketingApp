# 🔐 Authentication & Authorization Flows

## Authentication Methods

- **Email/Password**: Traditional username/password authentication
- **OAuth Integration**: Sign-in with Google and Microsoft accounts
- **JWT Implementation**: JSON Web Tokens for session management

## Token Management

- **Access Token**: 15-minute lifespan
- **Refresh Token**: 7-day lifespan, stored securely with HttpOnly cookies
- **Token Structure**: Header + Payload (user ID, role, team ID, expiration) + Signature

## Authentication Flow

1. User logs in via email/password or OAuth provider
2. Backend validates credentials and issues JWT access + refresh tokens
3. Client stores tokens (refresh token in HttpOnly cookie)
4. Access token sent in Authorization header for API requests
5. When access token expires, client uses refresh token to obtain new access token
6. If refresh token expires, user must re-authenticate

## RBAC (Role-Based Access Control)

- **Marketing Role**:
  - Full access to media, ads, and email group management
  - Can send emails to subscribers
  - Team-specific content access restrictions
- **Consumer Role**:
  - Read-only access to published ads
  - No access to email subscribers or backend features

## API Security

- `/auth/login`: Email/password authentication
- `/auth/refresh`: Obtain new access token using refresh token
- `/auth/oauth/{provider}`: Initiate OAuth flow
- `/auth/oauth/{provider}/callback`: OAuth provider callback
