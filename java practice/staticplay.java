class staticplay{
    static int a=3;
    static int b;
    static void f1(int x){
        System.out.println("x="+x);
        System.out.println("a="+a);
        System.out.println("b="+b);
    }
    static{
        System.out.println("staic block initialized");
        b=a*4;
    }
    public static void main(String[] args) {
        f1(42);
    }
}
