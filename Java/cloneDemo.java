import java.util.*;

class cloneDemo implements Cloneable{
	public static void main(String[] args)throws CloneNotSupportedException{
		cloneDemo cd = new cloneDemo();
		cd.display();
		
		cloneDemo cd1 = (cloneDemo)cd.clone(); 
		cd1.name = "xyz";
		cd1.display();
		
		cd1.a=1;
		cd1.b=2;
		cd1.date.setMonth(1);		
		cd1.display();
	}
	
	public cloneDemo clone() throws CloneNotSupportedException{
		cloneDemo cdd = (cloneDemo)super.clone();
		cdd.date = (Date) date.clone();
		return cdd;
	}
	
	int a = 10;
	int b = 20;
	String name = "abc";
	
	Date date = new Date();
	
	void display(){
		System.out.println("Variables: " + a + " " + b + " " + name);
		System.out.println("Date: " + date);
	}
}
