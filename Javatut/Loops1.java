import java.util.*;

class Loops1{
	public static void main(String han[]){
		Scanner read = new Scanner(System.in);
		System.out.println("Tiyambire kuwerenga pati?");
		int a = read.nextInt();
		System.out.println("Tilekezere pati kuwerenga?");
		int b = read.nextInt();
		System.out.println("Manambala ogawika ndi ziwiri ali motere");
		
		while(a<=b){
			if(a%2==0)
				System.out.print(a + "->");
			a++;
		}
		System.out.println("Basi");
		System.out.println();

	}

}
