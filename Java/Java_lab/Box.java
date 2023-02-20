package Java_lab;

public class Box {
    int width, length, height;

    Box(){
        super();
        this.width=this.length=this.height=10;
        }

    Box( int width, int length, int height){
        super();
        this.width = width;
        this.height=height;
        this.length=length;
        
    }
public void volume(){
    int volume = this.width *this.height *this.length;
    System.out.println(volume);
}
public static void main(String[] args) {
    
    Box b = new Box();
    b.volume();

    
    Box b2 = new Box(20,10,32);
    b2.volume();

}

    

}
