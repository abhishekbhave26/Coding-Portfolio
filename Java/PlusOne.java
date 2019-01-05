
    class PlusOne
    {
        public static void main(String[] args)
        {
            PlusOne p=new PlusOne();
            int new[]=new int[100];
            System.out.println(p.plusOne([2,4,7]));
            System.out.println(p.plusOne([2,9]));

        }
        public int[] plusOne(int[] digits)
        {
            int carry = 1;
            for (int i = digits.length-1; i>= 0; i--)
            {
                digits[i] += carry;
                if (digits[i] <= 9) // early return
                    return digits;
                digits[i] = 0;
            }
            int[] ret = new int[digits.length+1];
            ret[0] = 1;
            return ret;
        }
    }
