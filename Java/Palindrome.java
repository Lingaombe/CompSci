import java.util.*;

class Palindrome{

	public static void main(String han[]){
	
		Scanner scan = new Scanner(System.in);
		
		String a = scan.next();
		System.out.println(a);

		StringBuilder sb = new StringBuilder(a);
		
		sb.reverse();

		String b = sb.toString();
		System.out.println(b);
		
		if(a.equals(b)) {
			System.out.println("Palindrome");
		}else{
			System.out.println("Not Palindrome");
		}
	}

}
