import java.util.Scanner;
public class Stringreadingproblem{
    public static void main(String[]args){
        Scanner myinput = new Scanner(System.in);
        myinput.useDelimiter("\r?\n");
        System.out.println("Enter your number:" );
        int num= myinput.nextInt();
        System.out.println("Enter your float:" );
        float num1= myinput.nextFloat();
        System.out.println("Enter your String:" );
        String num2= myinput.next();

        myinput.close();

       
        System.out.println(num2);
        System.out.println(num1);
        System.out.println(num);
    }
}

