
# INPUT
starting_year = int(input("Enter the starting year : "))
ending_year = int(input("Enter the ending year : "))
per_credit = float(input("Enter per credit amount ($) : "))

# PROCESS 
initial_per_credit = per_credit
percentage_rate = 0.05
running_total = 0

print ("Year\tPer Credit Amount\tInterest\tRunning Total")
print("-"*60)
for year in range(starting_year, ending_year+1, 5):
    interest = per_credit * percentage_rate
    running_total = per_credit + interest
    # OUTPUT
    print(year,"\t%0.2f" % round(per_credit,2),
          "\t\t%0.2f" % round(interest,2),
          "\t\t%0.2f" % round(running_total,2))
    per_credit = running_total

total_interest = per_credit - initial_per_credit

# OUTPUT
print("-"*60)
print("Running Total : $" + str(round(running_total,2)))
print("Total Interest : $" + str(round(total_interest,2)))
