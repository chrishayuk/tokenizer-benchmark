fn main() {
    let numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100];
    let average = calculate_average(&numbers);
    println!("Average: {:.2}", average);

    let (min, max) = find_min_and_max(&numbers);
    println!("Minimum: {}", min);
    println!("Maximum: {}", max);
}

fn calculate_average(numbers: &[i32]) -> f64 {
    let sum: i32 = numbers.iter().sum();
    sum as f64 / numbers.len() as f64
}

fn find_min_and_max(numbers: &[i32]) -> (i32, i32) {
    let min = *numbers.iter().min().expect("Array cannot be empty");
    let max = *numbers.iter().max().expect("Array cannot be empty");
    (min, max)
}
