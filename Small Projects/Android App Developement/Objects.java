class Objects
{
  public static void main(String args[]) 
  {
    Student s = new Student();
    s.show_Total("gjfs",786,40,30,20);
  }
}
class Student
{
 str name; int roll_no;
 int mscore,pscore,cscore,total;
 void show_Total(str name,int roll_no,int mscore,int pscore,int cscore)
 {
  total=mscore+pscore+cscore;
  System.out.println("Name :"+name);
  System.out.println("Roll Number :"+roll_no);
  System.out.println("Math :"+mscore);
  System.out.println("Physics :"+pscore);
  System.out.println("Chemistry :"+cscore);
  System.out.println("Total :"+total);
  
 }
 
}