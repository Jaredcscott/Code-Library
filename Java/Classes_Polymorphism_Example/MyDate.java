/**
 * @author Jared Scott ☯
 * This class defines a MyDate object, as well as its getter and setter methods.
 */

public class MyDate {
	private int year;
	private int month;
	private int day;
	
	MyDate(int month, int day, int year) {
	    if (month < 0 || month > 11) {
	        System.out.println("Month entered is invalid, defaulting to January");
	        month = 0;
        }
		this.year = year;
		this.month = month;
		this.day = day;
	}
	
	String getMonthString() {
        //Returns a string of the name of the month in question 
        String monthString = "";
        switch (this.getMonth()) {
                case 0:
                    monthString = "January";
                    break;
                case 1:
                    monthString = "February";
                    break;
                case 2:
                    monthString = "March";
                    break;
                case 3:
                    monthString = "April";
                    break;
                case 4:
                    monthString = "May";
                    break;
                case 5:
                    monthString = "June";
                    break;
                case 6:
                    monthString = "July";
                    break;
                case 7:
                    monthString = "August";
                    break;
                case 8:
                    monthString = "September";
                    break;
                case 9:
                    monthString = "October";
                    break;
                case 10:
                    monthString = "November";
                    break;
                case 11:
                    monthString = "December";
                    break;
        }
        return monthString;
    }

	int getDay() {
        //Returns the day for the date
        return this.day;
    }
    
    int getMonth() {
        //Returns the month for the date
        return this.month;
    }

    int getYear() {
	    //Returns the year for the date
        return this.year;
    }

    void setDay(int day) {
	    //Sets the day
	    this.day = day;
    }

    void setMonth(int month) {
	    //Sets the month
	    this.month = month;
    }

    void setYear(int year) {
	    //Sets the year
	    this.year = year;
    }

    public String printDate() {
        //Prints date in the format of month dd, year
        String formatString = this.getMonthString() + " " + this.getDay() + ", " + this.getYear();
        return formatString;
    }
}