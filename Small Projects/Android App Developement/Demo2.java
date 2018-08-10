class A
{
  public int a = 5; // public variable. Accessible in child class which extends class A.
  private int c = 6; // private variable. Cannot be accessed outside class A.
  void superclass()
  {
    System.out.println("Super class" + " " + "value of a is " + a);
    System.out.println("Super class" + " " + "value of c is " + c);
  }
}
class B extends A
{
  int b = 7;
  int a = 8; //obtained from the parent class. Note that, c is private to class A and is not available in class B
  void subclass()
  {
    System.out.println("Sub class" + " " + "value of b is " + b);
    System.out.println("Sub class" + " " + "value of a is " + a);
  }
}
class Demo2
{
  public static void main(String args[])
  {
    A a1 = new A();
    B b1 = new B();
    a1.superclass();
    b1.subclass();
    b1.superclass();
  }
}