use std::net::{TcpListener, TcpStream};
use std::io::{Read, Write};

fn main() {
    let listener = TcpListener::bind("127.0.0.1:6379").unwrap();

    for stream in listener.incoming() {
        match stream {
            Ok(_stream) => {
                // Handle the connection (placeholder)
                println!("New connection established");

                let mut buffer = [0; 512];
                let mut stream = _stream;
                
                match stream.read(&mut buffer) {
                    Ok(_) => {
                        println!("Received: {}", String::from_utf8_lossy(&buffer[..]));
                        stream.write(b"+PONG\r\n").unwrap();
                    }
                    Err(e) => {
                        eprintln!("Failed to read from stream: {}", e);
                    }
                }
            }
            Err(e) => {
                eprintln!("Connection failed: {}", e);
            }
        }
    }
}
