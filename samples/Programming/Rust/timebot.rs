use futures_util::{StreamExt, SinkExt, stream::{SplitSink, SplitStream}};
use tokio::io::{AsyncRead, AsyncWrite};
use tokio::io::{self, AsyncBufReadExt};
use tokio_tungstenite::{connect_async, tungstenite::Message, WebSocketStream};

async fn register_bot(write: &mut SplitSink<WebSocketStream<impl AsyncRead + AsyncWrite + Unpin>, Message>, bot_name: &str) {
    let registration_message = Message::Text(format!("register as {}", bot_name));
    write.send(registration_message).await.expect("Failed to send registration message");
}

async fn handle_incoming_messages(mut read: SplitStream<WebSocketStream<impl AsyncRead + AsyncWrite + Unpin>>) {
    while let Some(message) = read.next().await {
        match message {
            Ok(msg) => println!("Received a message: {}", msg),
            Err(e) => eprintln!("Error receiving message: {}", e),
        }
    }
}

async fn read_and_send_messages(mut write: SplitSink<WebSocketStream<impl AsyncRead + AsyncWrite + Unpin>, Message>) {
    let mut reader = io::BufReader::new(io::stdin()).lines();
    while let Some(line) = reader.next_line().await.expect("Failed to read line") {
        if !line.trim().is_empty() {
            write.send(Message::Text(line)).await.expect("Failed to send message");
        }
    }
}


#[tokio::main]
async fn main() {
    let url = "ws://localhost:3000";

    println!("Connecting to - {}", url);
    let (ws_stream, _) = connect_async(url).await.expect("Failed to connect");
    println!("Connected to Agent Network");

    let (mut write, mut read) = ws_stream.split();

    // register the timebot
    register_bot(&mut write, "RustClient").await;

    // Handle incoming messages in a separate task
    let read_handle = tokio::spawn(handle_incoming_messages(read));

    // Read from command line and send messages
    let write_handle = tokio::spawn(read_and_send_messages(write));

    // Await both tasks (optional, depending on your use case)
    let _ = tokio::try_join!(read_handle, write_handle);
}