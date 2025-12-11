import java.util.*;

class Dec1{
	public static void main(String a[]){
		LinkedList<String> hehe = new LinkedList<String>();
		hehe.add("iwe");
		hehe.add("chilandamoyo");
		hehe.add("m'bale");
		hehe.add("inenso");
		hehe.add("mmelo");
		hehe.add(0,"malo");
		hehe.add("njala");
		hehe.add("ndekha");
		System.out.print("Original array: [");
		for( String i:hehe){
			System.out.print(i + ",");
		}
		System.out.print("]");
		System.out.println();
		System.out.println();
		System.out.print("Ordered array: [");
		Collections.sort(hehe);
		for( String i:hehe){
			System.out.print(i + ",");
		}
		System.out.print("]");
		System.out.println();
		System.out.println();
		System.out.print("Descending array: [");
		Collections.sort(hehe, Collections.reverseOrder());
		for( String i:hehe){
			System.out.print(i + ",");
		}
		System.out.print("]");
		System.out.println();
		
		for(int i =0; i<hehe.size(); i++){
			System.out.println(hehe.get(i));
		}
		
		Iterator<String> i = hehe.iterator();
		System.out.print(i.next() + " ");
		
		System.out.println();
		System.out.println(hehe.getFirst());
	}
}
