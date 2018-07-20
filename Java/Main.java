import java.util.Scanner;

public class Main
{
    int addMoney,account_number;



    public static void main(String []args)
    {

        Bank b=new Bank();


        b.addBalance(500);
        b.removeBalance(1000);

        Bank rohan=new Bank("Rohan","r","r");
        System.out.println("Customer name is "+rohan.getCustomer_name()+" balance is "+rohan.getBalance());


        /* VipBank p1=new VipBank();
        System.out.println(p1.getName()+" "+p1.getCredit_limit());

        VipBank p2=new VipBank("person 2",2000);
        System.out.println(p2.getName()+" "+p2.getCredit_limit()+" "+p2.getEmail());

        VipBank p3=new VipBank("person 3",50000,"p3@gmail.com");
        System.out.println(p3.getName()+" "+p3.getCredit_limit()+" "+p3.getEmail());
        */
    }

}
