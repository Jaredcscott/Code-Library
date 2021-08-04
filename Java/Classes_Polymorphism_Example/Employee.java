/**
 * @author Jared Scott
 * This class defines an Employee object, as well as its getter and setter methods.
 */

public class Employee extends Person {
    private String office;
    private double salary;
    private MyDate dateHired;

    Employee(String name, String address, String phoneNum, String emailAddr, String office, double salary,
             MyDate dateHired) {
        super(name,address,phoneNum,emailAddr);
        this.office = office;
        this.salary = salary;
        this.dateHired = dateHired;
    }

    String getOffice() {
        //Returns the office of the instance
        return this.office;
    }

    double getSalary() {
        //Returns the salary of the instance
        return this.salary;
    }

    MyDate getDateHired() {
        //Returns the date hired of the instance
        return this.dateHired;
    }

    void setOffice(String office) {
        //Sets the office
        this.office = office;
    }

    void setSalary(double salary) {
        //Sets the salary
        this.salary = salary;
    }

    void setDateHired(MyDate dateHired) {
        //Sets the date hired
        this.dateHired = dateHired;
    }

    @Override
    public String toString() {
        //Displays information about the instance in the form of a string.
        return "This is an Employee object\nName: " + this.getName();
    }
}