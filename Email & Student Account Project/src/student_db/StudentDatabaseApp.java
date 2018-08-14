package student_db;

import emailapp.Email;

import java.util.Scanner;

public class StudentDatabaseApp {
    public static void main(String[] args)
    {

        // ask for new users to add
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter number of students to add :");
        int number_of_students=sc.nextInt();




        // create students

        Student students[]=new Student[number_of_students];
        for(int n=0;n<number_of_students;n++)
        {
            students[n]=new Student();
            String firstName=students[n].getFirstName();
            String lastname=students[n].getLastName();
            int gradeYear=students[n].getGradeYear();

            Email em1=new Email(firstName,lastname);
            String password =em1.getPassword();
            String studentID=students[n].getStudentID();
            System.out.println(firstName+" "+lastname+" Grade Year:"+gradeYear+" Student ID: "+studentID);


            students[n].enroll();
            students[n].payTuition();
            System.out.println(students[n].showInfo());

        }


    }
}
