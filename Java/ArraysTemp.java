/*
 * Write a java program to read temperature for 15 days. Calculate average temperature and 
display the day numbers with temperature having temperature more than average, less than 
average and exactly equal to the average. 
 */

import java.util.Scanner;

public class ArraysTemp {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Store temperatures for 15 days
        double[] temps = new double[15];
        double sum = 0;

        // Read temperatures
        for (int i = 0; i < temps.length; i++) {
            System.out.print("Enter temperature for Day " + (i + 1) + ": ");
            temps[i] = sc.nextDouble();
            sum += temps[i];
        }

        // Calculate average
        double avg = sum / temps.length;
        System.out.println("\nAverage Temperature = " + avg);

        // Display days above average
        System.out.print("\nDays with temperature above average: ");
        for (int i = 0; i < temps.length; i++) {
            if (temps[i] > avg) {
                System.out.print("Day " + (i + 1) + " ");
            }
        }

        // Display days below average
        System.out.print("\nDays with temperature below average: ");
        for (int i = 0; i < temps.length; i++) {
            if (temps[i] < avg) {
                System.out.print("Day " + (i + 1) + " ");
            }
        }

        // Display days equal to average
        System.out.print("\nDays with temperature equal to average: ");
        for (int i = 0; i < temps.length; i++) {
            if (temps[i] == avg) {
                System.out.print("Day " + (i + 1) + " ");
            }
        }

        sc.close();
    }
}
