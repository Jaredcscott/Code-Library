/**
 * @author Jared Scott ☯
 * This class defines a Person object, as well as its getter and setter methods.
 */

public class Person {
    private String name;
    private String address;
    private String phoneNum;
    private String emailAddr;

    Person(String name, String address, String phoneNum, String emailAddr) {
        this.name = name;
        this.address = address;
        this.phoneNum = phoneNum;
        this.emailAddr = emailAddr;
    }

    String getName() {
        //Returns the name of the instance
        return this.name;
    }

    String getAddress() {
        //Returns the address of the instance
        return this.address;
    }

    String getPhoneNum() {
        //Returns the phone number of the instance
        return this.phoneNum;
    }

    String getEmailAddr() {
        //Returns the email address of the instance
        return this.emailAddr;
    }

    void setName(String name) {
        //Sets the name
        this.name = name;
    }

    void setAddress(String address) {
        //Sets the address
        this.address = address;
    }

    void setPhoneNum(String phoneNum) {
        //Sets the phone number
        this.phoneNum = phoneNum;
    }

    void setEmailAddr(String emailAddr) {
        //Sets the email address
        this.emailAddr = emailAddr;
    }

    @Override
    public String toString() {
        //Displays information about the instance in the form of a string.
        return "This is a Person object\nName: " + this.getName();
    }
}