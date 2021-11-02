'''
    @Author Jared Scott
    This file defines a class which can be used to watch a file for changes, when changes are made to the designated file, 
    the given function will be called with the provided arguments
'''
import os
import sys 
import time

class File_Watcher(object):
    refresh_delay_secs = 1                      #How often you want the watch to 'look'

    def __init__(self, watch_file, func_on_change=None, *args, **kwargs):
        self.running = True
        self._cached_stamp = 0                  # Used for detecting changes to the file 
        self.filename = watch_file              # File name 
        self.func_on_change = func_on_change    # Function which will be called upon change to file     
        self.args = args                        # Arguments for the function                     
        self.kwargs = kwargs                    # Keyworded arguments for the given function 

    # Look for changes
    def look(self):
        stamp = os.stat(self.filename).st_mtime
        if stamp != self._cached_stamp:
            self._cached_stamp = stamp
            # File has changed run on change function 
            print('File changed')
            if self.func_on_change is not None:
                self.func_on_change(*self.args, **self.kwargs)

           
    def watch(self):
        # Keep watching in a loop 
        while self.running: 
            try: 
                # Look for changes
                time.sleep(self.refresh_delay_secs) 
                self.look() 
            except KeyboardInterrupt: 
                print('Done') 
                break 
            except FileNotFoundError:
                # Action on file not found
                print("No file by name: " + self.filename + " found") 
                pass
            except: 
                print('Unhandled error: %s' % sys.exc_info()[0])
