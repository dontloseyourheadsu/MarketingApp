use std::net::{TcpListener, TcpStream};
use std::io::{Read, Write};

fn handle_connection(mut stream: TcpStream) {
    let mut buffer = [0; 512];
    
    match stream.read(&mut buffer) {
        Ok(bytes_read) => {
            let received = String::from_utf8_lossy(&buffer[..bytes_read]);
            println!("Received: {}", received.trim());
            
            // Write response - TCP handles MTU automatically
            let response = b"+PONG\r\n";
            match stream.write_all(response) {
                Ok(_) => println!("Response sent"),
                Err(e) => eprintln!("Failed to send response: {}", e),
            }
        }
        Err(e) => {
            eprintln!("Failed to read from stream: {}", e);
        }
    }
}

fn main() {
    let listener = TcpListener::bind("127.0.0.1:6379").unwrap();

    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                println!("New connection established");
                handle_connection(stream);
            }
            Err(e) => {
                eprintln!("Connection failed: {}", e);
            }
        }
    }
}