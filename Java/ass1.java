/*
Define a class MyNumber having one private int data member. Write a default  constructor to initialize it to 0 and another constructor to initialize it to a value (Use this). Write methods isNegative, isPositive, isZero, isOdd, isEven. Create an object in main. Use command line arguments to pass a value to the object.
*/

class MyNumber{
	private int member;
	
	MyNumber(){
		member = 0;
	}
	
	MyNumber(this){
		member = this.value();
	}
	
	void isNegative(member){}
	
	void isPositive(member){}
	
	void isZero(member){}
	
	void isOdd(member){}
	
	void isEven(){}
	
	public static void main(String[] args){
		MyMember mm = new MyMember();
		int x = Interger.parseInt(args[1]);
		
		mm.isNegative(x);
	}
}
