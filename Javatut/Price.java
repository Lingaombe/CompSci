//byte + short + int + long (whole), float + double (fraction), boolean (T/F) and char(ASCII value or char) primitive. always hold value and cant call methods
//Array, Classes, String non-primitive aka reference types because they refer to objects can be null and call methods.
//public accessible from anywhere, static can be called without creating an instance, void no return value, main is the entry point of the program
//String[] args is an array of strings that can be used to pass command line arguments
//System.out.println prints to the console
// semicolons braces help parsing
//void means what to return so String int so on

class Price{
    public static void main(String[] args) {
        int mtengo = 1000;
        char ndalama = 'K';
        int kuchuluka = 4;
        int mtengoWathunthu = mtengo * kuchuluka;
        System.out.println("Mtengo wa zinthu zanu ndi: " + ndalama + mtengoWathunthu );
    }
}