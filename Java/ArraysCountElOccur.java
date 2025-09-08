/*
 * Write a java program to create an array of certain size which will hold the integer elements 
and display the count of occurrences of each element. 
 */

public class ArraysCountElOccur {
    public static void main(String[] args) {

        int[] arr = {1, 20, 6, 40, 1};
        int occurence = 0;
        for(int i:arr){
            for(int j: arr){
                if(i==j){
                    occurence++;
                }
            }
            System.out.println(i + " occurs " + occurence + " times");
            occurence = 0;
        }
    }
}
