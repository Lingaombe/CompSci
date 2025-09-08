
public class LeftRightK {
    public static void main(String[] args) {
       int n = 3; // number of rows

        for (int i = 1; i <= n; i++) {
            // Left triangle
            for (int j = 1; j <= i; j++) {
                System.out.print("* ");
            }

            // Middle spaces
            int spaces = 2 * (n - i);
            for (int j = 1; j <= spaces; j++) {
                System.out.print("  "); // adjust spaces
            }

            // Right triangle
            for (int j = 1; j <= i; j++) {
                System.out.print("* ");
            }

            System.out.println();
        }
    }
}
