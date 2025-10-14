class AbstractClasses extends AbstractDemo{
	int b;
	AbstractClasses(){
		b = 20;
	}
	
	void addition(){
		System.out.println("Sum is " + (a+b));
	}
	
	public static void main(String[] args){
		AbstractClasses ac = new AbstractClasses();
		ac.addition();
		ac.display();
	}
}

abstract class AbstractDemo{
	int a = 10;
	final void display(){
		System.out.println(a);
	}
	abstract void addition();
}
