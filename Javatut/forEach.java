import java.util.*;

class forEach{

	public static void main(String han[]){
	
		Scanner scan = new Scanner(System.in);
		
		System.out.println("Enter length of array");
		
		int l = scan.nextInt();
		
		int ar[] = new int[l];

		for(int i = 0;i<ar.length;i++){
			System.out.println("Enter " + i +"th element");
			int el = scan.nextInt();
			ar[i] = el;
		}
	
		/*System.out.println("Array elements are");
		for(int x:ar){
			System.out.println(x);
		} */
		
		System.out.println("Enter number to check against");
		int n = scan.nextInt();
		int less = 0; int great = 0;
		
		for(int x:ar){
			if(x<n) less++;
			else great++;
		}
		
		System.out.println("Number of array elements less than "+ n +" are " + less);
		System.out.println("Number of array elements greater than "+ n +" are "+ great);
	}

}
