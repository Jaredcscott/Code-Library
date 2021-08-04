/**
 * @author Jared Scott
 * This class instantiates and tests the various classes within this program.
 */

public class TestSchool {
    public static void main(String[] args) {
        //Instantiating a Person object, calling its toString method and one of its getter methods
        Person person = new Person("Jimmy", "123 lane, Logan UT", "801-123-4567", "jimmyjohn@gmail.com");
        System.out.println(person.toString());
        System.out.println("Calling address getter method\nAddress: " + person.getAddress() + "\n");

        //Instantiating a Student object, calling its toString method and one of its getter methods
        Student student = new Student("Sally", "By the Sea Shore", "801-111-2222", "sallysellsseashells@yahoo.com", "Junior");
        System.out.println(student.toString());
        System.out.println("Calling class status getter method\nClass status: " + student.getClassStatus() + "\n");

        //Instantiating a Employee object, calling its toString method and one of its getter methods
        Employee employee = new Employee("Harry", "Private Drive, cupboard under the stairs", "801-223-2454", "Owl", "Hogwarts", 12.0, new MyDate(5,15,2014));
        System.out.println(employee.toString());
        System.out.println("Calling the salary getter method\nSalary: " + employee.getSalary() + "\n");

        //Instantiating a Faculty object, calling its toString method and one of its getter methods
        Faculty faculty = new Faculty("Jackson", "Engineer BLVD", "801-991-2827", "jacksongraham@hotmail.com", "EL 121", 25.5, new MyDate(3,18,2001), "Mon: 4 - 6", "Professor");
        System.out.println(faculty.toString());
        System.out.println("Calling the rank getter method\nRank: " + faculty.getRank() + "\n");

        //Instantiating a Staff object, calling its toString method and one of its getter methods
        Staff staff = new Staff("Ramon", "Dutro street", "425-777-2762", "ramonisnice@gmail.com", "Shop Floor", 13.50, new MyDate(4,5,1955), "Cleaner/Tube bender");
        System.out.println(staff.toString());
        System.out.println("Calling the title getter method\nTitle: " + staff.getTitle());
    }
}