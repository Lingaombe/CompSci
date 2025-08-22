import java.util.*;

class Conditionals1{
	public static void main(String args[]){
		Scanner read = new Scanner(System.in);
		System.out.println("Enter number: ");
		int a=read.nextInt();
		if(a>0) System.out.println("Entered value is: Positive");
		else if(a<0) System.out.println("Entered value is: Negative");
		else System.out.println("Entered value is: Zero");		
	}	
}
