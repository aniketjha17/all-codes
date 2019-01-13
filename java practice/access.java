// class VariableVisibility {
 
// 	private int a=12;
 
// 	public int getA() {
// 		return a;
// 	}
// }

// public class access {
// 	public static void main(String[] args) {
		
// 		VariableVisibility ob= new VariableVisibility();
// 		System.out.println(ob.getA());
// 	}
 
// }

class a{
    private int display(){
        int a=45;
        // System.out.println(+a);
        return a;
    }
    public int f1(){
        return display();
    }

}
class access{
    public static void main(String[] args) {
        a ob=new a();
        System.out.println(ob.f1());
    }
}





