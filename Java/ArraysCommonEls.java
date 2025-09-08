/*
 * Write a java program to create two arrays of certain size which will hold the integer elements 
and display the common elements from the both arrays. 
 */

public class ArraysCommonEls {
    public static void main(String[] args) {

        int[] arr2 = {1, 20, 6, 40, 7};
        int[] arr1 = {1, 9, 7, 4, 1};
        for(int i:arr1){
            for(int j:arr2){
                if(i==j) System.out.println(i+ " is common");
            }
        }
    }
}
