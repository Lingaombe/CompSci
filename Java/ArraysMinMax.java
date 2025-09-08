/*
 * Write a java program to create an array of certain size which will hold the integer elements 
    and display minimum and maximum number element from the array elements. 
 */

import java.util.Arrays;

public class ArraysMinMax {
    public static void main(String[] args) {

        int[] arr = {10, 20, 30, 40, 1};
        Arrays.sort(arr);
        System.out.println("Maximum: " + arr[0] + " Minimum: "+ arr[arr.length-1]);
    }
}
