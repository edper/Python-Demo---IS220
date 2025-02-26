# INPUT
initial_amount = float(input("Enter the invest amount : "))
years = int(input("Enter the number of years : "))
rate = int(input("Enter the rate as %: "))

# PROCESS
starting_balance = initial_amount
total_interest = 0

# Display the table header
print("%-6s%-18s%-10s%-15s" %  
     ("Year","Starting Balance","Interest","Ending Balance"))

# Display line detail
for year in range(years):
    interest = starting_balance * (rate / 100)
    ending_balance = starting_balance + interest
    total_interest += interest
    print("%4d%18.2f%10.2f%15.2f" % 
          (year+1,starting_balance, interest, ending_balance))
    starting_balance += interest
    
# Display Totals
print("Ending Balance:","$%8.2f" % ending_balance)
print("Total interest earned:","$%8.2f" % total_interest)
