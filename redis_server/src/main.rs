use std::net::{TcpListener, TcpStream};
use std::io::{Read, Write};

fn main() {
    let listener = TcpListener::bind("127.0.0.1:6379").unwrap();

    for stream in listener.incoming() {
        match stream {
            Ok(_stream) => {
                // Handle the connection (placeholder)
                println!("New connection established");
            }
            Err(e) => {
                eprintln!("Connection failed: {}", e);
            }
        }
    }
}
