package com.java_learning;

public class Power_of_3
{
    public static void main(String[] args)
    {
        Power_of_3 p=new Power_of_3();
        System.out.println(p.isPowerOfThree(81));

    }
    public boolean isPowerOfThree(int n)
    {
        double i,temp=0;
        if(n==0)
            return false;
        if(n==1)
            return true;
        for(i=1;i<=n/2;i++)
        {
            temp=Math.pow(3,i);
            if(temp==n)
            {
                return true;
            }
            else
                continue;
        }
        return false;

    }
}