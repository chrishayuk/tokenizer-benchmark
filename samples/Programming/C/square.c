#include <stdio.h>

int main() {
    int number, square;

    // Prompt the user for input
    printf("Enter an integer: ");
    
    // Read an integer from the user
    scanf("%d", &number);

    // Calculate the square of the number
    square = number * number;

    // Print the result
    printf("The square of %d is %d.\n", number, square);

    return 0;
}
