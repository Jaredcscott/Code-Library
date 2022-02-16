'''
    @Author Jared Scott ☯
    This function will use the windows API to set the system clock (SETS UTC TIME VALUE). 
    Adjust the values in the main function to obtain the desired system time. 
    NOTES ON TIME VALUES: 
    ---TIME IS IN UTC TIME--- 
        UTC 0:00  = 12:00 am 
        UTC 23:00 = 11:00 pm 
'''
import win32api

def main(OFFSETS):
    #---CHANGE THESE VALUES---
    YEAR         = 2022
    MONTH        = 1
    DAY_OF_MONTH = 1
    TIME_ZONE    = 'UTC'
    HOUR         = 9
    MINUTE       = 13
    SECOND       = 0 
    MILLISECOND  = 0
    #-------------------------
    TZO = OFFSETS[TIME_ZONE] #TIME ZONE OFFSET
    DAY_OF_WEEK  = 0
    time_tuple = (    YEAR,         # Year
                      MONTH,        # Month
                      DAY_OF_WEEK,  # Week Day
                      DAY_OF_MONTH, # Day 
                      HOUR + TZO,   # Hour NOTE: Computer may automatically adjust for timezone, check system time zone setting before use 
                      MINUTE,       # Minute
                      SECOND,       # Second
                      MILLISECOND,  # Millisecond
                  )
    # win32api.SetSystemTime(year, month , dayOfWeek , day , hour , minute , second , milliseconds)
    win32api.SetSystemTime(*time_tuple)

#---USA TIME ZONE OFFSETS---    
OFFSETS = {
    'UTC':0,
    'PDT':8,
    'MST':7,
    'MDT':6,
    'CDT':5,
    'EDT':4,
}   
MONTH_DAYS = {
    '1':31,
    '2':28,
    '3':31,
    '4':30,
    '5':31,
    '6':30,
    '7':31,
    '8':31,
    '9':30,
    '10':31,
    '11':30,
    '12':31,
}
LEAP_YEARS = [2000,2004,2008,2012,2016,2020,2024,2028,2032,2036,2040,2044,2048,2052,2056,2060,2064,2068,2072,2076,2080,2084,2088,2092,2096,3000]

if __name__ == "__main__": 
    main(OFFSETS)
    
