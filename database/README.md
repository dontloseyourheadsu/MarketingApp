# Database Setup - SurrealDB

SurrealDB setup for the Marketing App with schema and Docker configuration.

## Quick Start

```bash
cd database/
./setup.sh      # Start SurrealDB container
```

## Files

- `docker-compose.yml` - SurrealDB container configuration
- `schema.surql` - Database schema (SurrealQL)
- `schema.md` - Visual database diagram (Mermaid)
- `setup.sh` - Start SurrealDB container
- `README.md` - This file

## Connection Info

- **URL**: `http://localhost:8000`
- **Username**: `root` | **Password**: `root`

## Schema Overview

The database includes these main tables:

- **organizations** - Companies with settings and branding
- **users** - Organization members with roles
- **media** - Images/videos with metadata
- **advertisements** - Marketing content with targeting
- **subscribers** - Email list members with preferences
- **email_groups** - Subscriber segments
- **email_campaigns** - Scheduled email sends
- **organization_topics** - Content categories

See `schema.md` for a visual diagram of the relationships.

## Using with Rust

Add to your `Cargo.toml`:

```toml
[dependencies]
surrealdb = "2.0"
tokio = { version = "1", features = ["full"] }
serde = { version = "1", features = ["derive"] }
```

Example connection:

```rust
use surrealdb::engine::remote::ws::{Client, Ws};
use surrealdb::opt::auth::Root;
use surrealdb::Surreal;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let db = Surreal::new::<Ws>("localhost:8000").await?;

    db.signin(Root {
        username: "root",
        password: "root",
    }).await?;

    // Create namespace and database as needed
    db.use_ns("marketing").use_db("app").await?;

    // Your queries here...

    Ok(())
}
```

Example connection code:

```rust
use surrealdb::engine::remote::ws::{Client, Ws};
use surrealdb::opt::auth::Root;
use surrealdb::Surreal;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let db = Surreal::new::<Ws>("localhost:8000").await?;

    db.signin(Root {
        username: "root",
        password: "root",
    }).await?;

    db.use_ns("marketing").use_db("app").await?;

    // Query data
    let organizations: Vec<Organization> = db.select("organizations").await?;

    Ok(())
}
```

## Basic Queries

```sql
-- Get all organizations
SELECT * FROM organizations;

-- Get users with their organizations
SELECT *, ->works_for->organizations AS orgs FROM users;

-- Count records
SELECT count() FROM organizations GROUP ALL;
```

## Stop Database

```bash
docker-compose down     # Stop container
docker-compose down -v  # Stop and remove data
```
