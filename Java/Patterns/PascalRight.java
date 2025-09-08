
public class PascalRight {
    public static void main(String[] args) {
       int i, j;
        int n = 3;

        // outer loop to handle upper part
        for (i = 1; i <= n; i++) {
            
            // inner loop to print stars
            for (j = 1; j <= i; j++) {
                System.out.print("* ");
            }

            System.out.println();
        }

        // outer loop to handle lower part
        for (i = n-1; i >= 1; i--) {
            
            // inner loop to print stars
            for (j = 1; j <= i; j++) {
                System.out.print("* ");
            }

            System.out.println();
        }
    }
}
