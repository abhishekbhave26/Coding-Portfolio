import java.util.ArrayList;
import java.util.List;
public class Main8
{
    public static void main(String[] args)
    {
        selfDividingNumbers(1,82);


    }

    public static List<Integer> selfDividingNumbers(int left, int right)
    {
        ArrayList<Integer> list = new ArrayList<>();
        int n=0,i;
        for(int number=left;number<=right;number++)
        {
            i=number;
            int number_temp=number;
            int count=0,c_count=0;
            while(number_temp>0)
            {
                n=number_temp%10;
                if(n==0)
                {
                    break;
                }
                c_count++;
                if(number%n==0)
                {
                    count++;
                }
                number_temp=number_temp/10;
            }
            if(count==c_count&& n!=0)
            {
                list.add(i);
                System.out.println(i+" is added");
            }

        }
        return list;
    }

}