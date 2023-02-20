import java.util.*;
public class Reverse{
    public static void main(String[]args){
        int rem=0;
        int sum=0;
        Scanner myinput=new Scanner(System.in);
        int n = myinput.nextInt();
        myinput.close();
        
        if (n<9 && n>0){
            System.out.print("The reverse of the given number is "+n);
            
        }
        else{
            while (rem>0){
                rem = n%10;
                sum = sum*10 + rem;
            }
            System.out.print("The reverse of the given number is " +n);
           

        }

        
    }
}
