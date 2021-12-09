/**
 *
 * @author Jared Scott ☯
 * This class defines a Gregorian date. 
 *
 */


public class GregorianDate {
    private int yearGre;
    private int monthGre;
    private int dayGre;
    private boolean isCurrent;
    
    
    public GregorianDate() {
        this.isCurrent = true;
        this.yearGre = getCurrentYear();
        this.monthGre = getCurrentMonth();
        this.dayGre = getCurrentDayOfMonth();
    }
    
    
    public GregorianDate(int year, int month, int day) {
        this.isCurrent = false;
        this.yearGre = year;
        this.monthGre = month;
        this.dayGre = day;
    }
    
    
    void addDays(int days) {
        //Adds of "days" number of days onto the date
        this.dayGre += days;
        if(this.isLeapYear()) {
            while (this.dayGre > this.getNumberOfDaysInMonth()) {
                this.dayGre -= this.getNumberOfDaysInMonth();
                this.monthGre += 1;
                if(this.monthGre > 12) {
                    this.monthGre = 1;
                    this.yearGre += 1;
                }   
            }   
        }
        else {
            while (this.dayGre > this.getNumberOfDaysInMonth()) {
                this.dayGre -= this.getNumberOfDaysInMonth();
                this.monthGre += 1;
                if(this.monthGre > 12) {
                    this.monthGre = 1;
                    this.yearGre += 1;
                }
            }
        }
    }
    
    
    void subtractDays(int days) {
        //Subtracts "days" number of days from the date
        this.dayGre -= days;
        if(this.isLeapYear()) {
            while (this.dayGre < 1) {
                this.monthGre -= 1;
                if(this.monthGre < 1) {
                    this.monthGre = 12;
                    this.yearGre -= 1;
                }
                this.dayGre += this.getNumberOfDaysInMonth();
            }   
        }
        else {
            while (this.dayGre < 1) {
                this.monthGre -= 1;
                if(this.monthGre < 1) {
                    this.monthGre = 12;
                    this.yearGre -= 1;
                }
                this.dayGre += this.getNumberOfDaysInMonth();
            }
        }
    }
    
    
    boolean isLeapYear() {
        //Returns a bool of whether the year in question is a leap year
        if ((this.yearGre % 4 == 0 && this.yearGre % 100 != 0) || (this.yearGre % 100 == 0 && this.yearGre % 400 == 0)) {
            return true;
        }
        else{
            return false;
        }
    }
    
    
    void printShortDate() {
        //Prints date in the format of mm/dd/yyyy
        String formatString = this.monthGre + "/" + this.dayGre + "/" + this.yearGre;
        System.out.print(formatString);
    }
    
    
    void printLongDate() {
        //Prints date in the format of month dd, year
        String formatString = this.getCurrentMonthName() + " " + this.dayGre + ", " + this.yearGre;
        System.out.print(formatString);
    }
    
    
    String getCurrentMonthName() {
        //Returns a string of the name of the month in question 
        String monthString = "";
        switch (this.monthGre) {
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
        //Calculates the current month
        if (this.isCurrent) {
            int leapYears = 0;
            for (int i = 1970; i < this.yearGre; i++) {
                if (i % 4 == 0) {
                    leapYears += 1;
                }
            }
            double milliSec = System.currentTimeMillis();
			milliSec += java.util.TimeZone.getDefault().getRawOffset();
            double hours = milliSec / (1000 * 60 * 60);
            double days = (hours / 24) - (leapYears - 1); //This is to account for the additional days from leap years
            int remainingDays = (int)days % 365;
            if (remainingDays < 31) {
                return 1;
            }
            else if ((remainingDays > 31 && remainingDays <= 59) && !this.isLeapYear()) {
                return 2;
            }
            else if ((remainingDays > 59 && remainingDays <= 90) && !this.isLeapYear()) {
                return 3;
            }
            else if ((remainingDays > 90 && remainingDays <= 120) && !this.isLeapYear()) {
                return 4;
            }
            else if ((remainingDays > 120 && remainingDays <= 151) && !this.isLeapYear()) {
                return 5;
            }
            else if ((remainingDays > 151 && remainingDays <= 181) && !this.isLeapYear()) {
                return 6;
            }
            else if ((remainingDays > 181 && remainingDays <= 212) && !this.isLeapYear()) {
                return 7;
            }
            else if ((remainingDays > 212 && remainingDays <= 243) && !this.isLeapYear()) {
                return 8;
            }
            else if ((remainingDays > 243 && remainingDays <= 273) && !this.isLeapYear()) {
                return 9;
            }
            else if ((remainingDays > 273 && remainingDays <= 304) && !this.isLeapYear()) {
                return 10;
            }
            else if ((remainingDays > 304 && remainingDays <= 334) && !this.isLeapYear()) {
                return 11;
            }
            else if ((remainingDays > 334 && remainingDays <= 365) && !this.isLeapYear()) {
                return 12;
            }
            else if ((remainingDays > 31 && remainingDays <= 60) && this.isLeapYear() == true) {
                return 2;
            }
            else if ((remainingDays > 60 && remainingDays <= 91) && this.isLeapYear() == true) {
                return 3;
            }
            else if ((remainingDays > 91 && remainingDays <= 121) && this.isLeapYear() == true) {
                return 4;
            }
            else if ((remainingDays > 121 && remainingDays <= 152) && this.isLeapYear() == true) {
                return 5;
            }
            else if ((remainingDays > 152 && remainingDays <= 182) && this.isLeapYear() == true) {
                return 6;
            }
            else if ((remainingDays > 182 && remainingDays <= 213) && this.isLeapYear() == true) {
                return 7;
            }
            else if ((remainingDays > 213 && remainingDays <= 244) && this.isLeapYear() == true) {
                return 8;
            }
            else if ((remainingDays > 244 && remainingDays <= 274) && this.isLeapYear() == true) {
                return 9;
            }
            else if ((remainingDays > 274 && remainingDays <= 305) && this.isLeapYear() == true) {
                return 10;
            }
            else if ((remainingDays > 305 && remainingDays <= 335) && this.isLeapYear() == true) {
                return 11;
            }
            else if ((remainingDays > 335 && remainingDays <= 366) && this.isLeapYear() == true) {
                return 12;
            }
        }
        return this.monthGre;
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
        return this.yearGre;

    }

    
    int getNumberOfDaysInMonth() {
        //Returns the number of days in the month in question
        int[] monthNonLeap = {31,28,31,30,31,30,31,31,30,31,30,31};
        int[] monthLeap = {31,29,31,30,31,30,31,31,30,31,30,31};
        if (this.isLeapYear()) {
            return monthLeap[this.monthGre - 1];
        }
        else{
            return monthNonLeap[this.monthGre -1];
        }
    }

    
    int getCurrentDayOfMonth() {
        //Calculates the current day
        if (this.isCurrent) {
            int leapYears = 0;
            int[] monthNonLeap = {31,28,31,30,31,30,31,31,30,31,30,31};
            int[] monthLeap = {31,29,31,30,31,30,31,31,30,31,30,31};
            for (int i = 1970; i < this.yearGre; i++) {
                if (i % 4 == 0) {
                    leapYears += 1;
                }
            }
            double milliSec = System.currentTimeMillis();
            milliSec += java.util.TimeZone.getDefault().getRawOffset();
            double hours = milliSec / (1000 * 60 * 60);
            double days = (hours / 24) - (leapYears - 1); //This is to account for the additional days from leap years
            int remainingDays = (int)days % 365;
            if(this.isLeapYear()) {
                for (int j = 0; j < 12; j++) {
                    if(remainingDays > monthLeap[j]) {
                        remainingDays -= monthLeap[j];
                    }
                }
            }
            else {
                for(int k = 0; k < 12 ; k++) {
                    if(remainingDays > monthNonLeap[k]) {
                        remainingDays -= monthNonLeap[k];
                    }
                }
            }
            return remainingDays;
        }
        else {
            return this.dayGre;
        }
    }
}