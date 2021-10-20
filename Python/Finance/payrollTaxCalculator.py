'''
    @author:Jared Scott

    Asks the user for inputs regarding an employees pay information.
    The program will perform some calculations on those inputs and output the
    employees pay/tax information to the user.
'''

employeeName = (input("Enter employee's name: ")).upper()
numOfHoursWorked = round(float(input("Enter number of hours worked in a week: ")),4)
hourlyRate = round(float(input("Enter hourly pay rate: ")),4)
federalTaxRate = round(float(input("Enter federal tax witholding rate (ex 0.12): ")),4)
stateTaxRate = round(float(input("Enter state tax witholding rate (ex. 0.06): ")),4)
grossPay = numOfHoursWorked * hourlyRate
federalTax = grossPay * federalTaxRate
stateTax = grossPay * stateTaxRate
deductionsTotal = federalTax + stateTax
federalTaxRate = federalTaxRate * 100
stateTaxRate = stateTaxRate * 100
netPay = grossPay - deductionsTotal
header = "\n{0:^55}\n\n".format(employeeName + " PAY INFORMATION")
pay = "{0:^55}\n{1:>35}{2:>10}\n{3:>35}{4:>10}\n{5:>35}{6:>10}\n\n"\
       .format("Pay","Hours Worked:  ","%.2f"%numOfHoursWorked,"Pay Rate: $",
               "%.2f"%hourlyRate,"Gross Pay: $","%.2f"%grossPay)
deductions = "{0:^55}\n{1:>35}{2:>10}\n{3:>35}{4:>10}\n{5:>35}{6:>10}\n\n{7:>35}{8:>10}"\
              .format("Deductions","Federal Withholding ({0}%): $".format("%.2f"%federalTaxRate),
                      "%.2f"%federalTax,"State Withholding ({0}%): $".format("%.2f"%stateTaxRate),
                      "%.2f"%stateTax,"Total Deduction: $","%.2f"%deductionsTotal,
                      "Net Pay: $","%.2f"%netPay)
print(header,pay,deductions)
