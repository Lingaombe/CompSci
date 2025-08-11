import java.io.*;

class While{
	public static void main(String han[]) throws IOException{
	
		InputStreamReader reader = new InputStreamReader(System.in);
		BufferedReader read = new BufferedReader(reader);
		
		System.out.println("Tiyambire kuwerenga pati?");
		int a = Integer.parseInt(read.readLine());
		System.out.println("Tilekezere pati kuwerenga?");
		int b = Integer.parseInt(read.readLine());
		System.out.println("evens from "+a +" to " + b +" : ");
		
		while(a<=b){
			if(a!=0 && a%2==0)
				System.out.print(a + "->");
			a++;
		}
		System.out.println("Basi");
		System.out.println();

	}

}
