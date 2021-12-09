/**
 *
 * @author Jared Scott ☯
 * This class defines a generic date
 *
 */


public class Date {
    
    protected int year;
    protected int month;
    protected int day;
    protected boolean isCurrent;
    
    protected void addDays(int days) {
        //Adds of "days" number of days onto the date
        this.day += days;
        if(this.isLeapYear()) {
            while (this.day > this.getNumberOfDaysInMonth()) {
                this.day -= this.getNumberOfDaysInMonth();
                this.month += 1;
                if(this.month > 12) {
                    this.month = 1;
                    this.year += 1;
                }   
            }   
        }
        else {
            while (this.day > this.getNumberOfDaysInMonth()) {
                this.day -= this.getNumberOfDaysInMonth();
                this.month += 1;
                if(this.month > 12) {
                    this.month = 1;
                    this.year += 1;
                }
            }
        }
    }
    
    
    protected void subtractDays(int days) {
        //Subtracts "days" number of days from the date
        this.day -= days;
        if(this.isLeapYear()) {
            while (this.day < 1) {
                this.month -= 1;
                if(this.month < 1) {
                    this.month = 12;
                    this.year -= 1;
                }
                this.day += this.getNumberOfDaysInMonth();       
            }   
        }
        else {
            while (this.day < 1) {
                this.month -= 1;
                if(this.month < 1) {
                    this.month = 12;
                    this.year -= 1;
                }
                this.day += this.getNumberOfDaysInMonth();
            }
        }
    }
    
    
    protected void printShortDate() {
        //Prints date in the format of mm/dd/yyyy
        String formatString = this.month + "/" + this.day + "/" + this.year;
        System.out.print(formatString);
    }
    
    
    protected void printLongDate() {
        //Prints date in the format of month dd, year
        String formatString = this.getCurrentMonthName() + " " + this.day + ", " + this.year;
        System.out.print(formatString);
    }
    
    
    protected String getCurrentMonthName() {
        //Returns a string of the name of the month in question 
        String monthString = "";
        switch (this.month) {
                case 1:
                    monthString = "January";
                    break;
                case 2:
                    monthString = "February";
                    break;
                case 3:
                    monthString = "March";
                    break;
                case 4:
                    monthString = "April";
                    break;
                case 5:
                    monthString = "May";
                    break;
                case 6:
                    monthString = "June";
                    break;
                case 7:
                    monthString = "July";
                    break;
                case 8:
                    monthString = "August";
                    break;
                case 9:
                    monthString = "September";
                    break;
                case 10:
                    monthString = "October";
                    break;
                case 11:
                    monthString = "November";
                    break;
                case 12:
                    monthString = "December";
                    break;
        }
        return monthString;
    }
    
    
    protected int getNumberOfDaysInMonth() {
        //Returns the number of days in the month in question
        int[] monthNonLeap = {31,28,31,30,31,30,31,31,30,31,30,31};
        int[] monthLeap = {31,29,31,30,31,30,31,31,30,31,30,31};
        if (this.isLeapYear()) {
            return monthLeap[this.month - 1];
        }
        else{
            return monthNonLeap[this.month -1];
        }
    }
    
    
    boolean isLeapYear() {
        //This is to be overridden by the subclasses
        return true;
    }
    
    
    protected int getCurrentDayOfMonth() {
        //Returns the current day of the month for the date
        return this.day;
    }
    
    protected int getCurrentMonth() {
        //Returns the current month for the date
        return this.month;
    }

    protected int getCurrentYear() {
        //Calculates the current year
        if (this.isCurrent) {
            double milliSec = System.currentTimeMillis();
            milliSec += java.util.TimeZone.getDefault().getRawOffset();
            double years = milliSec / (1000 * 60 * 60 * 24 * 7 * 52.1429);
            int currentYear = 1970 + (int) years;
            return currentYear;
        }
        return this.year;
    }
}