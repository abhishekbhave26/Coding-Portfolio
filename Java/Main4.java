public class Main4
{
    public static void main(String[] args)
    {
        Printer p=new Printer(50,true);
        p.fillToner(30);
        int x=p.printPage(7);
        System.out.println("Pages printed was : "+x);
        p.fillToner(50);
        int z=p.getTonerLevel();
        System.out.println("Toner level is : "+z);

    }
}
