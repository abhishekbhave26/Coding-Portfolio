// class for implementing VIP bank

public class VipBank
{
    private String name,email;
    private double credit_limit;

    public String getName() {
        return name;
    }

    public double getCredit_limit() {
        return credit_limit;
    }
    public String getEmail() {

        return email;
    }

    public VipBank()
    {
        this("aniket",50000,"aniket@gmail.com");
    }
    public VipBank(String name, double credit_limit) {
        this(name,credit_limit,"unknown");
    }

    public VipBank(String name,double credit_limit,String email) {
        this.name = name;
        this.email = email;
        this.credit_limit = credit_limit;
    }



}
