/**
 * @author Jared Scott
 * This class defines a Faculty object, as well as its getter and setter methods.
 */

public class Faculty extends Employee {
    private String officeHours;
    private String rank;

    Faculty(String name, String address, String phoneNum, String emailAddr, String office, double salary,
            MyDate dateHired, String officeHours, String rank){
        super(name,address,phoneNum,emailAddr,office,salary,dateHired);
        this.officeHours = officeHours;
        this.rank = rank;
    }

    String getOfficeHours() {
        //Returns the office hours
        return this.officeHours;
    }

    String getRank() {
        //Returns the rank
        return this.rank;
    }

    void setOfficeHours(String officeHours) {
        //Sets the office hours
        this.officeHours = officeHours;
    }

    void setRank(String rank) {
        //Sets the rank
        this.rank = rank;
    }

    @Override
    public String toString() {
        //Displays information about the instance in the form of a string.
        return "This is a Faculty object\nName: " + this.getName();
    }
}