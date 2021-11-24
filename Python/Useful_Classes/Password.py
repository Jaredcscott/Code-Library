'''
    @Author Jared Scott ☯
    This file defined the class Password, and defines its needed methods.
    This password enforces the following requirements:
        Password length <= 8 characters
        Password must consist of only numbers and letters
        Password must contain at least 2 numbers
        Password cannot contain the word password
        Password cannot end with "123"
'''

def main():
    pw = Password()
    pw.tryPassword("helloiam1122aweakpassw0rd") #Replace this string to try a different password. 

class Password:
    def __init__(self):
        self.__message = ""
        self.__attempt = ""
        self.__password = ""
        self.__eightCharactors = False
        self.__onlyCharAndDigit = False
        self.__hasTwoDigits = False
        self.__noPassword = False
        self.__no123Ending = False
        self.__numOfDigits = 0
        self.__allTrue = False


    def setPassword(self,attempt):
        self.__resetBools()
       
        self.__password = attempt


    def tryPassword(self,attempt):
        self.__resetBools()
        self.__attempt = attempt
        if self.isValid():
            print("All requirements met, password set")
            self.setPassword(attempt)
        else:
            self.getErrorMessage()


    def __getLength(self):
        return len(self.__attempt)


    def __isAlphaNum(self):
        return self.__attempt.isalnum()


    def __noPasswordIn(self):
        if "PASSWORD" in self.__attempt.upper():
            return False
        else:
            return True


    def __no123AtEnding(self):
        lastIndex = self.__getLength()
        if self.__attempt[lastIndex-3:lastIndex] == "123":
            return False
        else:
            return True


    def getErrorMessage(self):
        print("\nINVALID PASSWORD: \n" + self.__message)


    def __resetBools(self):
        self.__eightCharactors = False
        self.__onlyCharAndDigit = False
        self.__hasTwoDigits = False
        self.__noPassword = False
        self.__no123Ending = False
        self.__numOfDigits = 0
        self.__allTrue = False


    def isValid(self):
        self.__message = ""
        index = 0
        if self.__getLength() >= 8:
            self.__eightCharactors = True
        else:
            self.__message += "Must have 8 characters\n"

        if self.__isAlphaNum():
            self.__onlyCharAndDigit = True
        else:
            self.__message += "Must only contain letters and digits\n"

        self.__numOfDigits = 0
        while index < self.__getLength():
            if self.__attempt[index].isdigit():
                self.__numOfDigits += 1
            index += 1
        if self.__numOfDigits >= 2:
            self.__hasTwoDigits = True
        else:
            self.__message += "Must have at least 2 digits\n"

        if self.__noPasswordIn():
            self.__noPassword = True
        else:
            self.__message += "Must not contain the word \"password\"\n"

        if self.__no123AtEnding():
            self.__no123Ending = True
        else:
            self.__message += "Cannot end with 123\n"

        if self.__eightCharactors and self.__onlyCharAndDigit and self.__hasTwoDigits and self.__noPassword and self.__no123Ending:
            self.__allTrue = True
        if not self.__allTrue:
            self.getErrorMessage()
        return self.__allTrue
    
if __name__ == '__name__':
    main()
