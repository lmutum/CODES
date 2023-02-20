import java.util.*;
public class Oddupto {
    public static void main(String[]args){
        Scanner myinput = new Scanner(System.in);
            System.out.print("Enter your number: ");
            int n = myinput.nextInt();
            myinput.close();
            System.out.print("The odd numbers upto "+n +" are : ");
            for(int i=1 ; i <=n ; i++){
                if (i%2!=0){
                    System.out.print(i+" ");
                }
            }
            
    }
    
}
