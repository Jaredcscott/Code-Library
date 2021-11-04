'''
    @Author Jared Scott ☯
    Takes 3 inputs from the user, an interest rate, a loan amount, and a number of years.
    Performs some calculations and outputs an investment value after the given time period.
'''

annualInterestRate = eval(input("Enter the annual interest rate as a percentage. eg 8.25: ")) / 100
investmentAmount = eval(input("Enter an investment amount: "))
numYears = eval(input("Enter number of years: "))
monthlyInterestRate = annualInterestRate / 12
futureInvestmentValue = investmentAmount * ((1 + monthlyInterestRate)**(numYears * 12))
futureInvestmentValue = str(round(futureInvestmentValue, 2))

print("The future value of your investment is: " + futureInvestmentValue)
