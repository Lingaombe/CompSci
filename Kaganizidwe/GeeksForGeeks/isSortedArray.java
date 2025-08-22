import java.util.*;

class isSortedArray {
    public static boolean isSorted(int[] arr) {
        int ar1[];
        ar1 = arr;
        Arrays.sort(ar1);
        System.out.println(Arrays.toString(ar1));
        
        int sorted = Arrays.compare(arr,ar1);
        System.out.println(sorted);
        if(sorted != 0){
            return true;
        }else{
            return false;
        }
    }
    public static void main(String[] args){
        int arr[] = {1,4,5};
        System.out.println(isSorted(arr));
    }
}