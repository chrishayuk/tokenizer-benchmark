use rand::Rng; // Rng trait defines methods that random number generators implement
use std::cmp::Ordering; // For comparing the guess to the secret number
use std::io; // For input/output operations

fn main() {
    println!("Guess the number!");

    // Generate a random number between 1 and 100
    let secret_number = rand::thread_rng().gen_range(1..=100);

    loop {
        println!("Please input your guess.");

        let mut guess = String::new();

        // Read the user's guess from standard input
        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");

        // Convert the string to a number
        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("Please type a number!");
                continue;
            },
        };

        // Compare the guess to the secret number
        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win!");
                break; // Exit the loop if the guess is correct
            },
        }
    }
}
