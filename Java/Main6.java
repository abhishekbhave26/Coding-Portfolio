// mobile phone contacts application in java

import java.sql.SQLOutput;
import java.util.ArrayList;
import java.util.Scanner;

public class Main6
{
    private static Scanner sc=new Scanner(System.in);
    private static MobilePhone mobilePhone=new MobilePhone("2222222");

    public static void main(String[] args) {
        boolean quit=false;
        startPhone();
        printAction();

        while(!quit){
            System.out.println("\n Enter action :(6 to show available action)");
            int action=sc.nextInt();
            sc.nextLine();

            switch (action)
            {
                case 0:
                    System.out.println("Shutting down");
                    quit=true;
                    break;

                case 1:
                    mobilePhone.printContacts();
                    break;

                case 2:
                    addContacts();
                    break;

                case 3:
                    updateContact();
                    break;

                case 4:
                    removeContact();
                    break;

                case 5:
                    queryContact();
                    break;

                case 6:
                    printAction();
                    break;


            }
        }


    }
    private static void addContacts()
    {
        System.out.println("Add new contact name");
        String name=sc.nextLine();
        System.out.println("Enter phone number");
        String phone=sc.nextLine();
        Contacts contacts=Contacts.createContact(name,phone);
        if(mobilePhone.addContact(contacts))
            System.out.println("New contact added");
        else
            System.out.println("Cannot add, name already exists");
    }

    private static void updateContact(){
        System.out.println("enter existing name");
        String name=sc.nextLine();
        Contacts existingContact=mobilePhone.queryContact(name);
        if(existingContact==null){
            System.out.println("Contact not found");
            return;
        }
        System.out.println("Enter new contact name");
        String newName=sc.nextLine();
        System.out.println("Enter contact number");
        String newNumber=sc.nextLine();
        Contacts newContact=Contacts.createContact(newName,newNumber);
        if(mobilePhone.updateContact(existingContact,newContact))
        System.out.println("Successfully updated record");
        else
            System.out.println("Error in updating");
    }
    private static void removeContact() {
        System.out.println("enter existing name");
        String name = sc.nextLine();
        Contacts existingContact = mobilePhone.queryContact(name);
        if (existingContact == null) {
            System.out.println("Contact not found");
            return;
        }
        if(mobilePhone.removeContact(existingContact))
            System.out.println("Successfully deleted");
        else
            System.out.println("Error in deletion");
    }
    private static void queryContact() {
        System.out.println("enter existing name");
        String name = sc.nextLine();
        Contacts existingContact = mobilePhone.queryContact(name);
        if (existingContact == null) {
            System.out.println("Contact not found");
            return;
        }
        System.out.println("Name: "+existingContact.getName()+" Phone Number :"+existingContact.getPhoneNumber());

    }


    private static void startPhone(){
        System.out.println("Starting Phone ....");
    }

    private static void printAction(){
        System.out.println("\n Available actions : press");
        System.out.println("0 - Shutdown \n"+
                            "1 - Print contacts \n"+
                            "2 - Add contact \n"+
                            "3 - Update existing contact \n "+
                            "4 - Remove contact \n "+
                            "5 - Query existing contact \n"+
                            "6 - Print list of available actions");
        System.out.println("Enter option");
    }

}









class MobilePhone
{
    private String myNumber;
    private ArrayList<Contacts> myContacts;

    public MobilePhone(String myNumber){
        this.myNumber=myNumber;
        this.myContacts=new ArrayList<Contacts>();
    }

    public boolean addContact(Contacts contacts )
    {
        if (findContact(contacts.getName())>=0){
            System.out.println("Contact already exists");
            return false;
        }
        myContacts.add(contacts);
        return true;
    }
    public void printContacts(){
        System.out.println("Contact List");
        for(int i=0;i<this.myContacts.size();i++)
            System.out.println((i+1) +"."+this.myContacts.get(i).getName()+"-> "+this.myContacts.get(i).getPhoneNumber());
    }

    private int findContact(Contacts contacts){
        return this.myContacts.indexOf(contacts);
    }

    public Contacts queryContact(String name){
        int position=findContact(name);
        if(position>=0)
        {
            return this.myContacts.get(position);
        }
        return null;
    }


    private int findContact(String contactName){
        for(int i=0;i<this.myContacts.size();i++){
            Contacts contacts=this.myContacts.get(i);
            if(contacts.getName().equals(contactName))
                return i;
        }
        return -1;
    }

    public boolean updateContact(Contacts oldContact,Contacts newContact){
        int foundPosition=findContact(oldContact);
        if(foundPosition<0)
        {
            System.out.println(oldContact.getName()+" was not found");
            return false;
        }
        else if(findContact(newContact.getName())!=-1)
        {
            System.out.println("Contact with this name already exists");
            return false;
        }
        this.myContacts.set(foundPosition,newContact);
        System.out.println(oldContact.getName()+" changes to "+newContact.getName());
        return true;
    }

    public String queryContact(Contacts contacts){
        if(findContact(contacts)>=0)
            return contacts.getName();
        return null;
    }

    public boolean removeContact(Contacts contacts){
        int foundPosition=findContact(contacts);
        if(foundPosition<0)
        {
            System.out.println(contacts.getName()+" was not found");
            return false;
        }
        this.myContacts.remove(foundPosition);
        System.out.println(contacts.getName()+"was deleted");
        return true;
    }
}













class Contacts
{
    private String name,phoneNumber;

    public Contacts(String name, String phoneNumber) {
        this.name = name;
        this.phoneNumber = phoneNumber;
    }

    public String getName() {
        return name;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public static Contacts createContact(String name,String phoneNumber)
    {
        return new Contacts(name,phoneNumber);
    }
}
