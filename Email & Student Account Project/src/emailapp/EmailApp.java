package emailapp;

public class EmailApp
{
    public static void main(String[] args) {
        //Email em1=new Email("Abhishek","Bhave");
        Email em2=new Email("John","Doe");
        em2.changePassword("johndoe1960");
        System.out.println("Password is "+em2.getPassword());
    }
}
