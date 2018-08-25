package student_db;

import java.util.Scanner;

public class Student {

    private String firstName, lastName, courses, studentID;
    private int tuitionBalance = 0, gradeYear;
    private static int ID = 1000, costOfCourse = 600;

    
	//constructor


    public Student() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter student first name:");
        this.firstName = sc.nextLine();

        System.out.println("Enter student last name:");
        this.lastName = sc.nextLine();

        System.out.println("Enter student grade year: \n1 Freshman \n2 Sophomore \n3 Junior \n4 Senior ");
        this.gradeYear = sc.nextInt();

        studentID = setstudentID();


    }


    // generate id
    private String setstudentID() {
        ID++;
        return gradeYear + "" + ID;

    }


    // enroll in courses
    public void enroll() {

        do {
            System.out.print("Enter course to enroll (Q to quit) :");
            Scanner sc = new Scanner(System.in);
            String course = sc.nextLine();
            if (!course.equals("Q")) {
                courses = courses + "\n  " + course;
                tuitionBalance += costOfCourse;
            } else {
                break;
            }
        }
        while (1 != 0);


    }


    // view balance

    public void getTuitionBalance() {
        System.out.println("Your balance is :$" + tuitionBalance);
    }


    // pay tuition
    public void payTuition()
    {
        Scanner sc=new Scanner(System.in);
        getTuitionBalance();
        System.out.print("Enter the amount you want to pay :");
        int payment=sc.nextInt();
        tuitionBalance-=payment;
        System.out.println("Thank you for your payment of :$"+payment);
        getTuitionBalance();

    }

    // show status
    public String showInfo()
    {
        return "Name : "+firstName+" "+lastName+"\nGrade Level : "+gradeYear+"\nStudent ID : "+studentID+"\nCourses Enrolled :"+courses
        +"\nBalance is :"+tuitionBalance;


    }

	getters

    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public int getGradeYear() {
        return gradeYear;
    }
    public String getStudentID() {
        return studentID;
    }

}
