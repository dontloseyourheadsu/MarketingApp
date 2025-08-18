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

- Frontend: Leptos (Rust WebAssembly)
- Backend: Axum (Rust)
- Database: SurrealDB
- Authentication: JWT, OAuth (SurrealDB built-in)
- Storage: SurrealDB (replaces traditional object storage)

## Getting Started

### Prerequisites

Install Rust and required tools:

```bash
# Install Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source ~/.cargo/env

# Add WebAssembly target
rustup target add wasm32-unknown-unknown

# Install Trunk for serving the frontend
cargo install trunk

# Ensure Docker is installed and running for SurrealDB
# Ubuntu/Debian: sudo apt install docker.io docker-compose
# macOS: Install Docker Desktop
# Windows: Install Docker Desktop
```

### Running the Application

1. **Database** (from `/database` directory):

   ```bash
   ./setup.sh
   ```

2. **Frontend** (from `/frontend` directory):

   ```bash
   trunk serve --open
   ```

3. **Backend** (from `/backend` directory):
   ```bash
   cargo run
   ```
