public class Bank
{
    private long account_number,balance;
    private String customer_name,email,phone_no;

    public Bank()
    {
        this(115,5000,"a","a","a");
        System.out.println("empty");
    }
    public Bank(long account_number,long balance,String customer_name,String email,String phone_no)
    {
        this.account_number=account_number;
        this.balance=balance;
        this.customer_name=customer_name;
        this.email=email;
        this.phone_no=phone_no;
    }
    public Bank(String customer_name, String email, String phone_no) {
        this(999,15000,customer_name,email,phone_no);
        this.customer_name = customer_name;
        this.email = email;
        this.phone_no = phone_no;
    }

    public void setAccount_number(long account_number)
    {
        this.account_number=account_number;
    }
    public void setBalance(long balance)
    {
        this.balance=balance;
    }
    public void setCustomer_name(String customer_name)
    {
        this.customer_name=customer_name;
    }
    public void setEmail(String email)
    {
        this.email=email;
    }
    public void setPhone_no(String phone_no)
    {
        this.phone_no=phone_no;
    }

    public long getAccount_number()
    {
        return this.account_number;
    }



    public long getBalance()
    {
        return this.balance;
    }
    public String getCustomer_name()
    {
        return this.customer_name;
    }
    public String getEmail()
    {
        return this.email;
    }
    public String getPhone_no()
    {
        return this.email;
    }
    public void addBalance(int addMoney)
    {
        this.balance+=addMoney;
        System.out.println("New balance is "+this.balance);
    }
    public void removeBalance(int removeMoney)
    {
        if(this.balance >= removeMoney)
        {
            this.balance -= removeMoney;
            System.out.println("Removing money of "+removeMoney+" processed");
            System.out.println("New balance is "+this.balance);
        }
        else
        {
            System.out.println("Balance is not sufficient");
        }
    }
}
