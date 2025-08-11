use axum::{routing::get, Router};
use std::net::SocketAddr;

async fn ping() -> &'static str { "pong" }

#[tokio::main]
async fn main() {
    let app = Router::new().route("/ping", get(ping));

    let addr = SocketAddr::from(([0, 0, 0, 0], 3000));
    axum::serve(tokio::net::TcpListener::bind(addr).await.unwrap(), app)
        .await
        .unwrap();
}
