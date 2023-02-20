import java.util.*;
public class prime {
    public static void main(String args[]){
        Scanner myinput = new Scanner(System.in);
        System.out.print("Enter your number: ");
        int n = myinput.nextInt();
        myinput.close();        
        if(n ==0 || n==1){
                System.out.print("The given number "+n+" is not a prime number.");
        }
       else {
            int  i=2;
            int A = 0;
                while (i<=n/2){
                    if (n%i==0){
                        A = 0 ;                        
                    }
                    else{
                        A = 1;
                    }
                    i=i+1;
                                        }
                if (A == 0){
                    System.out.print("The given number "+n+" is not a prime number.");
                }
                else{
                    System.out.print("The given number "+n+" is a prime number.");
                }
                            }
                    }
                }
                    
    
    
