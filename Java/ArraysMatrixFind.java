/*
 * Write a java program to guess the number from two dimensional array. 
Example 
Display Matrix 
1 2 3 
4 5 6 
7 8 9 
Ask user to enter column number like 1 or 2 or 3 in which his number is present. 
Read column number. 
Eg. Column number 2 
Shuffle the array by replacing first row with the column number given by the user. Display 
the array. 
2 5 8 
3 6 9 
1 4 7 
Ask user to enter column number like 1 or 2 or 3 in which his number is present. 
Read column number. 
Eg. Column number 3 
You can guess the number as 8. 
 */

import java.util.Scanner;

public class ArraysMatrixFind {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Original matrix
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        // Step 1: Display matrix
        System.out.println("Original Matrix:");
        displayMatrix(matrix);

        // Step 2: Ask first column
        System.out.print("Enter column number (1-3) where your number is: ");
        int col1 = sc.nextInt() - 1; // adjust index

        // Step 3: Shuffle - make chosen column the first row
        int[][] newMatrix = new int[3][3];
        for (int i = 0; i < 3; i++) {
            newMatrix[0][i] = matrix[i][col1]; // chosen column becomes first row
        }

        // Fill rest rows with remaining numbers
        int r = 1;
        for (int i = 0; i < 3; i++) {
            if (i != col1) {
                for (int j = 0; j < 3; j++) {
                    newMatrix[r][j] = matrix[j][i];
                }
                r++;
            }
        }

        // Step 4: Display new matrix
        System.out.println("\nShuffled Matrix:");
        displayMatrix(newMatrix);

        // Step 5: Ask second column
        System.out.print("Enter column number (1-3) where your number is now: ");
        int col2 = sc.nextInt() - 1;

        // Step 6: Guess number (it will be in first row, at col2)
        int guessedNumber = newMatrix[0][col2];
        System.out.println("\nI guessed your number: " + guessedNumber);

        sc.close();
    }

    // Utility function to print matrix
    private static void displayMatrix(int[][] mat) {
        for (int[] row : mat) {
            for (int val : row) {
                System.out.print(val + " ");
            }
            System.out.println();
        }
    }
}
