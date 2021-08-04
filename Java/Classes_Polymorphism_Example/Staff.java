/**
 * @author Jared Scott
 * This class defines a Staff object, as well as its getter and setter methods.
 */

public class Staff extends Employee {
    private String title;

    Staff(String name, String address, String phoneNum, String emailAddr, String office, double salary,
          MyDate dateHired, String title) {
        super(name,address,phoneNum,emailAddr,office,salary,dateHired);
        this.title = title;
    }

    String getTitle() {
        //Returns the title for the instance
        return this.title;
    }

    void setTitle(String title) {
        //Sets the title
        this.title = title;
    }

    @Override
    public String toString() {
        //Displays information about the instance in the form of a string.
        return "This is a Staff object\nName: " + this.getName();
    }
}