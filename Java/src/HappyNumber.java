import java.util.LinkedList;

public class HappyNumber
{
    public static void main(String[] args)
    {
        Solution s =new Solution();
        s.isHappy(155);

    }
}

class Solution {
    public boolean isHappy(int n) {

        int ncopy=n;
        int answer=0;
        LinkedList list=new LinkedList<Integer>();
        while(ncopy>0)
        {
            list.add(ncopy%10);
            ncopy=ncopy/10;
        }
        while(answer==1)
        {
            int i=0
            int x=list.get(0);

        }
    }
}
