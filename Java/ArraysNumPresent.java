// Write a java program to create an array of certain size which will hold the integer elements 
// and also read a number from user and find the given number is present within array or not. If 
// number found then display its index. 

import java.util.Scanner;

public class ArraysNumPresent {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int[] arr = {10, 20, 30, 40, 50};
        System.out.print("Number to check : ");
        int n = sc.nextInt();
        boolean present = false;
        int ind = 0;
        for(int i:arr){
            if(n==i){
                present = true;
                break;
            } 
            ind++;
        }
        System.out.println(present? "present at index: "+ind : "not present");
    }
}
