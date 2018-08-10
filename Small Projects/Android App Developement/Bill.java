import java.util.*;
class Bill
{
  public static void main(String args[])
  {
    Scanner sc =new Scanner(System.in);
	System.out.println("Enter amount of units");
	int units=sc.nextInt();
	float amt,tamt,mamt;
    if(units<100)
    {
		amt=units*1;
    }
    else if (units<200)
    {
        amt=units*2;
    }
	else if (units<300)
    {
        amt=units*3;
    }
	else if (units<500)
    {
        amt=units*4;
    }
    else
    {
        amt=units*5;
    }
	tamt=amt+(amt/10);
	mamt=tamt+50;
	System.out.println("your bill is "+mamt);
  }
}