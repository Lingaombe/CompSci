// Write a java program to create an array of certain size which will hold the integer elements 
// and display the sum and average of alternate elements.  

public class ArraysSumAvg {
     public static void main(String[] args) {

        int[] arr = {10, 20, 30, 40, 50};
        int sum = 0;
        int div = 0;
        for(int i=0;i<arr.length;i+=2){
            sum += arr[i];
            div++;
        }
        System.out.println("Sum: " + sum + " Average: "+ sum/div);
    }
}
