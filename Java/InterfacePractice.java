class InterfacePractice extends Act implements fight, fly{
	InterfacePractice(){
		super();
	}
	
	public void canFight(){
		System.out.println(actor + " can fight");
	}
	
	public void canFly(){
		System.out.println(actor + " can fly");
	}
	
	public static void main(String[] args){
		InterfacePractice ip = new InterfacePractice();
		ip.canFight();
		ip.canFly();
		ip.canAct();
	}
}

interface fight{
	void canFight();
}

interface fly{
	void canFly();
}

class Act{
	String actor;
	
	Act(){
		actor = "Manganya";
	}
	
	void canAct(){
		System.out.println(actor + " can act");
	}
}
