import java.util.*;
public class Fibonaci {
    public static void main(String[]args){
        Scanner myinput = new Scanner(System.in);
        System.out.print("Enter your number: ");
        int n= myinput.nextInt();
        myinput.close();
        int s1 = 0;
        int s2 = 1;
        int s3 = 0;
        System.out.print("The " + n + "th Fibonaci series are: ");
        if(n==0){
            ;
        }
        else{
            ;
            System.out.print(s1 +" ");
           // System.out.print(s2 +" ");
        }
        for(int i=1; i<n; i++){
            //System.out.print(s1+" ");
            s3 = s2 + s1;
            System.out.print(s2 + " ");
            s1=s2;
            s2=s3;

        }

    }
    
}
