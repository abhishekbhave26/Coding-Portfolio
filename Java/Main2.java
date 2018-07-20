public class Main2
{
    public static void main(String[] args)
    {
        boolean x = bark(true, 15);
        System.out.println(x);
    }




    public static void printMegaBytesAndKiloBytes(int kiloBytes) {
        int MB, KB;
        if (kiloBytes < 0)
            System.out.println("Invalid Value");
        MB = kiloBytes / 1024;
        KB = kiloBytes % 1024;
        System.out.println(kiloBytes + "KB = " + MB + " MB and " + KB + " KB");
    }

    public static boolean bark(boolean barking, int hourOfDay)
    {
        if (barking)
        {
            if (hourOfDay <= 8 || hourOfDay >= 22)
            {
                return true;
            }
        }

        return false;

    }
}