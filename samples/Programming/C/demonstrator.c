#include <stdio.h>

#define SIZE 10 // Define the size of the array

// Function prototypes
double calculateAverage(int arr[], int size);
void findMinAndMax(int arr[], int size, int *min, int *max);

int main() {
    int numbers[SIZE] = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
    double average;
    int min, max;

    // Calculate the average of the array
    average = calculateAverage(numbers, SIZE);
    printf("Average: %.2f\n", average);

    // Find the minimum and maximum values in the array
    findMinAndMax(numbers, SIZE, &min, &max);
    printf("Minimum: %d\n", min);
    printf("Maximum: %d\n", max);

    return 0;
}

// Function to calculate the average of an array
double calculateAverage(int arr[], int size) {
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += arr[i];
    }
    return (double)sum / size;
}

// Function to find the minimum and maximum values in an array
void findMinAndMax(int arr[], int size, int *min, int *max) {
    *min = *max = arr[0]; // Initialize min and max with the first element of the array
    for (int i = 1; i < size; i++) {
        if (arr[i] < *min) {
            *min = arr[i]; // Update min if the current element is smaller
        }
        if (arr[i] > *max) {
            *max = arr[i]; // Update max if the current element is larger
        }
    }
}