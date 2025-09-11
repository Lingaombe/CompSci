import java.util.Scanner;

public class EncodeDecode {
    static Scanner read = new Scanner(System.in);
    public static void main(String[] args){
        int choice = displayMessage();
        System.out.println("Enter shift i.e 2 for A-C etc");
        int shift = read.nextInt();
        processChoice(choice, shift);
    }
    public static int displayMessage(){
        System.out.println("Enter your numeric choice based on the menu");
        System.out.println("1. Encode");
        System.out.println("2. Decode");
        System.out.println("3. Exit");
        return read.nextInt();
    }
    public static void processChoice(int y, int z){
        System.out.print("Enter the message to encode/decode: ");
        String userMessage = read.next();
        if(y==1) encode(userMessage, z);
        else if(y==2) decode(userMessage, z);
        else if(y==3) displayMessage();
        else System.out.print("Invalid selection");
    }
    public static void encode(String x, int z){
        StringBuilder sb = new StringBuilder(x);
        for(int i=0;i<sb.length();i++){
            char c = sb.charAt(i);
            sb.setCharAt(i, (char) (c + z));
        }
        System.out.println("Decoded string: " + sb.toString());
    }
    public static void decode(String x, int z){
        StringBuilder sb = new StringBuilder(x);
        for(int i=0;i<sb.length();i++){
            char c = sb.charAt(i);
            sb.setCharAt(i, (char) (c - z));
        }
        System.out.println("Decoded string: " + sb.toString());
    }
}