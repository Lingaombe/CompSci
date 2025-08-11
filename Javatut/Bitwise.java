class Bitwise{
	public static void main(String[] args){
		int a=5;
		int b=10;
		System.out.println("Bitwise and of 5 and 10: " + (a&b));
		System.out.println("Bitwise or: " + (a|b));
		System.out.println("Bitwise exor: " + (a^b));
		System.out.println("Bitwise not: " + (~b));
		System.out.println("Bitwise not: " + (~a));
		System.out.println("Bitwise a right shift: " + (a>>2));
		System.out.println("Bitwise b shift: " + (b>>2));
		System.out.println(">>> 5: " + (a>>>2));
		System.out.println("Bitwise a left shift: " + (a<<2));
		System.out.println("Bitwise b shift: " + (b<<2));

		Bitwise obj = new Bitwise();
		System.out.println("obj is instance of class: " + (obj instanceof Bitwise));
	}
}
