/*
 *Write a java program to create items array with another to store their unit prices. Display item 
list to user to purchase, accept the quantity. Finally display the item purchased with its unit 
price, total of purchased item and final total bill. 
 */

import java.util.Scanner;

class ArrayUnitPrices{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Items and unit prices
        String[] items = {"Pen", "Notebook", "Pencil", "Eraser", "Bag"};
        double[] prices = {10.0, 50.0, 5.0, 3.0, 500.0};

        // To store purchased quantities
        int[] quantities = new int[items.length];

        // Display items list
        System.out.println("---- Item List ----");
        for (int i = 0; i < items.length; i++) {
            System.out.println((i + 1) + ". " + items[i] + " - Rs." + prices[i]);
        }

        // Accept purchase
        System.out.print("\nEnter number of items you want to buy: ");
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            System.out.print("Enter item number (1-" + items.length + "): ");
            int choice = sc.nextInt() - 1;

            if (choice >= 0 && choice < items.length) {
                System.out.print("Enter quantity for " + items[choice] + ": ");
                quantities[choice] += sc.nextInt();
            } else {
                System.out.println("Invalid item number, skipping...");
            }
        }

        // Display bill
        System.out.println("\n---- Final Bill ----");
        double finalTotal = 0;
        for (int i = 0; i < items.length; i++) {
            if (quantities[i] > 0) {
                double total = quantities[i] * prices[i];
                System.out.println(items[i] + " x " + quantities[i] +
                                   " @ Rs." + prices[i] + " = Rs." + total);
                finalTotal += total;
            }
        }

        System.out.println("--------------------");
        System.out.println("Total Bill = Rs." + finalTotal);

        sc.close();
    }
}