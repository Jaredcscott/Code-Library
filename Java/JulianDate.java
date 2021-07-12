/**
 *
 * @author Jared Scott
 * This class defines a Julian date
 *
 */

public class JulianDate {
    int yearJul;
    int monthJul;
    int dayJul;
    boolean isCurrent ;
    
    
    public JulianDate() {
        this.isCurrent = true;
        this.yearJul = 1;
        this.monthJul = 1;
        this.dayJul = 1;
        int leapYears = 0;
        for (int i = 1970; i < this.yearJul; i++) {
            if (i % 4 == 0) {
                leapYears += 1;
            }
        }
        double milliSec = System.currentTimeMillis();
        milliSec += java.util.TimeZone.getDefault().getRawOffset();
        double hours = milliSec / (1000 * 60 * 60);
        double days = (hours / 24) - (leapYears);
        this.addDays(719164 + (int) days);
    }
    
    
    public JulianDate(int year, int month, int day) {
        this.isCurrent = false;
        this.yearJul = year;
        this.monthJul = month;
        this.dayJul = day;   
    }
    
    
    void addDays(int days) {
        //Adds of "days" number of days onto the date
        this.dayJul += days;
        if(this.isLeapYear()) {
            while (this.dayJul > this.getCurrentDaysOfMonth()) {
                this.dayJul -= this.getCurrentDaysOfMonth();
                this.monthJul += 1;
                if(this.monthJul > 12) {
                    this.monthJul = 1;
                    this.yearJul += 1;
                }   
            }   
        }
        else {
            while (this.dayJul > this.getCurrentDaysOfMonth()) {
                this.dayJul -= this.getCurrentDaysOfMonth();
                this.monthJul += 1;
                if(this.monthJul > 12) {
                    this.monthJul = 1;
                    this.yearJul += 1;
                }
            }
        }
    }
    
    
    void subtractDays(int days) {
        //Subtracts "days" number of days from the date
        this.dayJul -= days;
        if(this.isLeapYear()) {
            while (this.dayJul < 1) {
                this.monthJul -= 1;
                if(this.monthJul < 1) {
                    this.monthJul = 12;
                    this.yearJul -= 1;
                }
                this.dayJul += this.getCurrentDaysOfMonth();       
            }   
        }
        else {
            while (this.dayJul < 1) {
                this.monthJul -= 1;
                if(this.monthJul < 1) {
                    this.monthJul = 12;
                    this.yearJul -= 1;
                }
                this.dayJul += this.getCurrentDaysOfMonth();
            }
        }
    }
    
    
    boolean isLeapYear() {
        //Returns a bool of whether the year in question is a leap year
        if(this.yearJul % 4 == 0) {
            return true;
        }
        else{
            return false;
        }
    }
    
    
    void printShortDate() {
        //Prints date in the format of mm/dd/yyyy
        String formatString = this.monthJul + "/" + this.dayJul + "/" + this.yearJul;
        System.out.print(formatString);
    }
    
    
    void printLongDate() {
        //Prints date in the format of month dd, year
        String formatString = this.getCurrentMonthName() + " " + this.dayJul + ", " + this.yearJul;
        System.out.print(formatString);
    }

    
    String getCurrentMonthName() {
        //Returns a string of the name of the month in question
        String monthString = "";
        switch (this.monthJul) {
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
	
    
    int getCurrentMonth() {
        return this.monthJul;
    }
    
    
    int getCurrentYear() {
        //Calculates the current year
        if (this.isCurrent) {
            double milliSec = System.currentTimeMillis();
            milliSec += java.util.TimeZone.getDefault().getRawOffset();
            double years = milliSec / (1000 * 60 * 60 * 24 * 7 * 52.1429);
            int currentYear = 1970 + (int) years;
            return currentYear;
        }
        return this.yearJul;
    }
    
    
    int getCurrentDaysOfMonth() {
        //Returns the number of days in the month in question
        int[] monthNonLeap = {31,28,31,30,31,30,31,31,30,31,30,31};
        int[] monthLeap = {31,29,31,30,31,30,31,31,30,31,30,31};
        if (this.isLeapYear()) {
            return monthLeap[this.monthJul - 1];
        }
        else {
            return monthNonLeap[this.monthJul - 1];
        }
    }


    int getCurrentDayOfMonth() {
        return this.dayJul;
    }
}