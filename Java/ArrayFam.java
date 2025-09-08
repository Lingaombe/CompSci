/*
 *  Write a java program to read count of family members and read the ages for all family 
members and store them in one-dimensional array and display the age of youngest and oldest 
member. 
 */

class ArratFam{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Read number of family members
        System.out.print("Enter number of family members: ");
        int n = sc.nextInt();

        // Create array to store ages
        int[] ages = new int[n];

        // Read ages
        for (int i = 0; i < n; i++) {
            System.out.print("Enter age of member " + (i + 1) + ": ");
            ages[i] = sc.nextInt();
        }

        // Initialize youngest and oldest
        int youngest = ages[0];
        int oldest = ages[0];

        // Find youngest and oldest
        for (int i = 1; i < n; i++) {
            if (ages[i] < youngest) youngest = ages[i];
            if (ages[i] > oldest) oldest = ages[i];
        }

        // Display results
        System.out.println("\nYoungest member's age: " + youngest);
        System.out.println("Oldest member's age: " + oldest);

        sc.close();
    }
}