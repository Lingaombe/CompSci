/*
 * Write a java program to accept the sales in figures (Lacks) for East, West, North and South 
Zones for 12 months. Calculate total and average sales of all zones and display it. Also 
display the zone name with highest total sale. 
 */

import java.util.Scanner;

class ArraySales{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[] zones = {"East", "West", "North", "South"};
        int months = 12;

        // 2D array to store sales
        double[][] sales = new double[zones.length][months];

        // Input sales data
        for (int i = 0; i < zones.length; i++) {
            System.out.println("Enter sales (in lakhs) for " + zones[i] + " Zone:");
            for (int j = 0; j < months; j++) {
                System.out.print("Month " + (j + 1) + ": ");
                sales[i][j] = sc.nextDouble();
            }
        }

        double[] totalSales = new double[zones.length];
        double[] avgSales = new double[zones.length];

        // Calculate totals and averages
        for (int i = 0; i < zones.length; i++) {
            double sum = 0;
            for (int j = 0; j < months; j++) {
                sum += sales[i][j];
            }
            totalSales[i] = sum;
            avgSales[i] = sum / months;
        }

        // Find highest total sale zone
        double maxSale = totalSales[0];
        String bestZone = zones[0];

        for (int i = 1; i < zones.length; i++) {
            if (totalSales[i] > maxSale) {
                maxSale = totalSales[i];
                bestZone = zones[i];
            }
        }

        // Display results
        System.out.println("\n--- Sales Report ---");
        for (int i = 0; i < zones.length; i++) {
            System.out.println(zones[i] + " Zone -> Total: " + totalSales[i] +
                               " lakhs, Average: " + avgSales[i] + " lakhs");
        }

        System.out.println("\nZone with highest total sales: " + bestZone +
                           " (" + maxSale + " lakhs)");

        sc.close();
    }
}