# Make a python program that will accept
# an investment amount and compute its
# total investment income along with its compounded interest. 
# Aside from investment amount
# as input include also the annual interest rate/percentage
# and the number of years of investment.
# For example for an investment of $100 with 5% in 3 years
# the total investment income would be $115.76
# And in this case the compounded interest or the earnings
# for the $100 is $15.76

# --Example--
# Enter investment amount ($) : 100
# Enter the annual interest rate (%) : 5
# Enter the number of years of investment : 3
# Your $100 will yield an interest of $15.76 in 3 years
# for a total of $115.76

# INPUT
investment_amount = float(input("Enter the investment amount ($) : "))
interest_rate = float(input("Enter the annual interest rate (%) : "))
years = int(input("Enter the number of years of investment : "))

# PROCESS 
principal = investment_amount
percentage_rate = interest_rate / 100

for year in range(years):
    interest = principal * percentage_rate
    principal = principal + interest

total_interest = principal - investment_amount
total_yield = principal

# OUTPUT
print("Your $"+str(investment_amount),"will yield an interest of $"
     + str(round(total_interest,2)),"in",years,"years, for a total of $" 
     + str(round(total_yield,2)))