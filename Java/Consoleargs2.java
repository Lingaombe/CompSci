import java.io.*;

class Consoleargs2{
	public static void main(String args[]) throws IOException{
		InputStreamReader reader = new InputStreamReader(System.in);
		BufferedReader read = new BufferedReader(reader);
		
		System.out.println("Enter first number");
		int a = Integer.parseInt(read.readLine());
		
		System.out.println("Enter second number");
		int b = Integer.parseInt(read.readLine());
		
		System.out.println("Sum of "+ a + " and " + b + " is " + (a+b));
	}

}
