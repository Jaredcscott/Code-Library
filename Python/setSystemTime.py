import win32api

time_tuple = ( 2021,  # Year
                  7,  # Month
                  2,  # Week Day
                  14, # Day
                  1,  # Hour
                 30,  # Minute
                  0,  # Second
                  0,  # Millisecond
              )
              
def _win_set_time(time_tuple):
    # pywin32.SetSystemTime(year, month , dayOfWeek , day , hour , minute , second , milliseconds)
    win32api.SetSystemTime( time_tuple[0],time_tuple[1],time_tuple[2],time_tuple[3],time_tuple[4],time_tuple[5],time_tuple[6],time_tuple[7])
    
_win_set_time(time_tuple)  