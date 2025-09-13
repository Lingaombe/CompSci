import java.util.Scanner;

public class EncodeDecode {
    static Scanner read = new Scanner(System.in);
    public static void main(String[] args){
        programEntry();
    }
    public static void programEntry(){
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
        switch(y){
            case 1:
                encode(userMessage, z);
                break;
            case 2:
                decode(userMessage, z);
                break;
            case 3:
                displayMessage();
                break;
            default:
                System.out.print("Invalid selection");
        }
    }
    public static void encode(String x, int z){
        StringBuilder sb = new StringBuilder(x);
        for(int i=0;i<sb.length();i++){
            char c = sb.charAt(i);
            if (Character.isLetter(c)) {
                if (Character.isUpperCase(c)) {
                    c = (char) ('A' + (c - 'A' + z + 26) % 26);
                } else {
                    c = (char) ('a' + (c - 'a' + z + 26) % 26);
                }
                sb.setCharAt(i, c);
            }
        }
        System.out.println("Encoded string: " + sb.toString());
        System.out.println();
        runAgain();
    }
    public static void decode(String x, int z){
        StringBuilder sb = new StringBuilder(x);
        for(int i=0;i<sb.length();i++){
            char c = sb.charAt(i);
            if (Character.isLetter(c)) {
                if (Character.isUpperCase(c)) {
                    c = (char) ('A' + (c - 'A' - z + 26) % 26);
                } else {
                    c = (char) ('a' + (c - 'a' - z + 26) % 26);
                }
                sb.setCharAt(i, c);
            }
        }
        System.out.println("Decoded string: " + sb.toString());
        System.out.println();
        runAgain();
    }
    
    public static void runAgain(){
        System.out.println("Do you wish to run again?");
        System.out.println("1. Yes or 2. No");
        int h = read.nextInt();
        if(h==1) programEntry();
        else System.out.println("Okay, exiting");
    }
}