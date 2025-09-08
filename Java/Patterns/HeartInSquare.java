
public class HeartInSquare {
    public static void main(String[] args) {
       int n = 5; // number of rows and columns

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                // Conditions for printing *
                if (i == 1 || i == 2 || i == n) { 
                    // First 2 rows & last row full stars
                    System.out.print("*   ");
                } 
                else if (i == 3 && (j <= 3 || j == n)) {
                    System.out.print("*   ");
                } 
                else if (i == 4 && (j <= 2 || j == n)) {
                    System.out.print("*   ");
                } 
                else {
                    System.out.print("    "); // spaces
                }
            }
            System.out.println();
        }
    }
}
