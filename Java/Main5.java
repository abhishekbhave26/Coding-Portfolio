// application to select burger and extras and price displayed

public class Main5
{
    public static void main(String[] args) {
      Hamburger h=new Hamburger("White","Sausage","Basic",3.50);

      h.addHamburgerAdd1("Tomato",0.55);
      h.addHamburgerAdd3("Cheese",1.25);
      h.addHamburgerAdd2("Chilly",0.74);
      double price=h.itemizeHamburger();
      System.out.println("Total price is "+price);
      System.out.println();

      Healthy he=new Healthy("Bacon",4.5);
      he.addHamburgerAdd1("Lettuce",1.5);
      he.addHealthAdd1("Greens",2.4);
      System.out.println("Total price is "+he.itemizeHamburger());
      System.out.println();

      Deluxe db=new Deluxe();

      db.addHamburgerAdd1("Fries",4);
        db.itemizeHamburger();
    }

}

class Hamburger
{
    private String bread_roll_type,meat,name;
    private double price;
    public Hamburger(String bread_roll_type, String meat, String name, double price)
    {
        this.bread_roll_type = bread_roll_type;
        this.meat = meat;
        this.name = name;
        this.price = price;
    }

    private String add1Name;
    private double add1Price;

    private String add2Name;
    private double add2Price;

    private String add3Name;
    private double add3Price;

    private String add4Name;
    private double add4Price;

    public void addHamburgerAdd1(String name,double price)
    {
        this.add1Name=name;
        this.add1Price=price;
    }
    public void addHamburgerAdd2(String name,double price)
    {
        this.add2Name=name;
        this.add2Price=price;
    }
    public void addHamburgerAdd3(String name,double price)
    {
        this.add3Name=name;
        this.add3Price=price;
    }
    public void addHamburgerAdd4(String name,double price)
    {
        this.add4Name=name;
        this.add4Price=price;
    }

    public double itemizeHamburger()
    {
        double hamburgerPrice=this.price;
        System.out.println(this.name +" hamburger on a "+this.bread_roll_type +" roll with " +this.meat+"and price is "+this.price);
        if(this.add1Name!=null)
        {
            hamburgerPrice+=this.add1Price;
            System.out.println("Added "+this.add1Name+" for an extra "+this.add1Price);
        }
        if(this.add2Name!=null)
        {
            hamburgerPrice+=this.add2Price;
            System.out.println("Added "+this.add2Name+" for an extra "+this.add2Price);
        }
        if(this.add3Name!=null)
        {
            hamburgerPrice+=this.add3Price;
            System.out.println("Added "+this.add3Name+" for an extra "+this.add3Price);
        }
        if(this.add4Name!=null)
        {
            hamburgerPrice+=this.add4Price;
            System.out.println("Added "+this.add4Name+" for an extra "+this.add4Price);
        }
        return hamburgerPrice;
    }

}


 class Healthy extends Hamburger
{
    private String healthyExtra1Name;
    private double healthyExtra1Price;

    private String healthyExtra2Name;
    private double healthyExtra2Price;

    public Healthy(String meat, double price) {
        super("Brown rye",meat,"Healthy", price);
    }
    public void addHealthAdd1(String name,double price)
    {
        this.healthyExtra1Name=name;
        this.healthyExtra1Price=price;
    }
    public void addHealthAdd2(String name,double price)
    {
        this.healthyExtra2Name=name;
        this.healthyExtra2Price=price;
    }

    @Override
    public double itemizeHamburger() {
        double hamburgerPrice=super.itemizeHamburger();
        if(this.healthyExtra1Name!=null)
        {
            hamburgerPrice+=this.healthyExtra1Price;
            System.out.println(this.healthyExtra1Name +"added for extra amount of"+this.healthyExtra1Price);
        }
        if(this.healthyExtra2Name!=null)
        {
            hamburgerPrice+=this.healthyExtra2Price;
            System.out.println(this.healthyExtra2Name +"added for extra amount of"+this.healthyExtra2Price);
        }
        return hamburgerPrice;
    }
}



class Deluxe extends Hamburger
{
    public Deluxe() {
        super("White","Ham","Deluxe",9);
        super.addHamburgerAdd1("Chips",4);
        super.addHamburgerAdd2("Drink",2);


    }

    @Override
    public void addHamburgerAdd1(String name, double price) {
        System.out.println("Cannot add additional items to a deluxe burger");
    }

    @Override
    public void addHamburgerAdd2(String name, double price) {
        System.out.println("Cannot add additional items to a deluxe burger");
    }

    @Override
    public void addHamburgerAdd3(String name, double price) {
        System.out.println("Cannot add additional items to a deluxe burger");
    }

    @Override
    public void addHamburgerAdd4(String name, double price) {
        System.out.println("Cannot add additional items to a deluxe burger");
    }
}

