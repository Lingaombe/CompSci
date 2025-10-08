import java.util.*;

public class Main {
    public static void main(String[] args) {
      int a[]={1,2,3,4};
      int b=0;
      
      try{
       System.out.println(a[4]);
      }
      catch
        (IndexOutOfBoundsException ioob){
          System.out.println("use index within bounds 0 to 3");
        }
        finally{
          System.out.println(Arrays.toString(a));
        }
  }
}