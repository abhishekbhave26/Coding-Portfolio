package emailapp;

import java.util.Scanner;

public class Email
{
    private String firstname,lastname,password,department,alternate_email,email;
    private int mailBoxCapacity=500;
    private int defaultpasswordLength=10;
    private String companySuffix="mycompany.com";

    // Constructor asks fname and lname

    public Email(String firstname, String lastname)
    {
        this.firstname = firstname;
        this.lastname = lastname;
        System.out.println("EMAIL CREATED FOR :"+this.firstname+" "+this.lastname);

        this.department=setDepartment();
        System.out.println("Department :"+this.department);

        this.password=randomPassword(defaultpasswordLength);
        System.out.println("Your password is "+this.password);

        email=firstname.toLowerCase()+"."+lastname.toLowerCase()+"@"+department+"."+companySuffix;
        System.out.println("Email is :"+email);


    }

    // ask dept
    private String setDepartment()
    {
        System.out.println("Enter the department \n1 Sales \n2 Development \n3 Accounting \n0 None");
        Scanner sc =new Scanner(System.in);
        int depChoice=sc.nextInt();
        if(depChoice==1)
            return "sales";
        else if(depChoice==2)
            return "dev";
        else if(depChoice==3)
            return "acct";
        else
            return "";

    }

    //generate random password
    private String randomPassword(int length)
    {
        String passwordSet="ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%";
        char password[]=new char[length];
        for(int i=0;i<length;i++)
        {
            int rand=(int)(Math.random()*passwordSet.length());
            password[i]=passwordSet.charAt(rand);
        }
        return new String(password);
    }



    //set mailbox capacity,set alt email,change password

    public void setAlternate_email(String alternate_email) {
        this.alternate_email = alternate_email;
    }

    public void setMailBoxCapacity(int mailBoxCapacity) {
        this.mailBoxCapacity = mailBoxCapacity;
    }

    public void changePassword(String password)
    {
        this.password=password;
    }




    // getters
    public String getPassword()
    {
        return password;
    }

    public String getAlternate_email() {
        return alternate_email;
    }

    public int getMailBoxCapacity() {
        return mailBoxCapacity;
    }




}
