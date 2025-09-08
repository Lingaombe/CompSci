public class MatrixSumDiff {

    public static void main(String[] args) {

        int[][] matrix1 = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        int[][] matrix2 = {
            {10, 11, 12},
            {13, 14, 15},
            {16, 17, 18}
        };

        int[][] sum = new int[3][3];       // matrix to store addition
        int[][] difference = new int[3][3]; // matrix to store subtraction

        // Perform addition and subtraction
        for (int i = 0; i < 3; i++) {         // row
            for (int j = 0; j < 3; j++) {     // column
                sum[i][j] = matrix1[i][j] + matrix2[i][j];
                difference[i][j] = matrix1[i][j] - matrix2[i][j];
            }
        }

        // Display addition result
        System.out.println("Addition of two matrices:");
        for(int[] i:sum){
            for(int j:i){
                System.out.print(j + " ");
            }
            System.out.println();
        }
        

        // Display subtraction result
        System.out.println("\nSubtraction of two matrices:");
        for(int[] i:difference){
            for(int j:i){
                System.out.print(j + " ");
            }
            System.out.println();
        }
    }

}
