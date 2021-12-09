/**
 * @author Jared Scott ☯
 * This class defines a Student object, as well as its getter and setter methods.
 */

public class Student extends Person {
    private String classStatus;

    Student(String name, String address, String phoneNum, String emailAddr, String classStatus) {
        super(name,address,phoneNum,emailAddr);
        this.classStatus = classStatus;
    }

    String getClassStatus() {
        //Returns the class status
        return this.classStatus;
    }

    void setClassStatus(String classStatus) {
        //Sets the class status
        this.classStatus = classStatus;
    }

    @Override
    public String toString() {
        //Displays information about the instance in the form of a string.
        return "This is a Student object\nName: " + this.getName();
    }
}