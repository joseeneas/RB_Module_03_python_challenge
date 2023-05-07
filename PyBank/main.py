import os
import csv

budget_data_csv = "/Users/eneas/desktop/bootcamp/repository/my-repository/python-challenge/PyBank/Resources/budget_data.csv"
output_file = "/Users/eneas/desktop/bootcamp/repository/my-repository/python-challenge/PyBank/Output/Bank_Analysis.csv"

# Lists to store data
date = 0    # This will hold the Month/Year information
pl = 0      # this will hold the profit/loss information
months = 0  # this will hold the number of months, assumint each line contains a different month
total = 0   # this will be used to accumulate the P/L.
greater=0   # This will hold the greatest increase
lower=0     # this will hold the greatest decrease

# opening the file and processing each line, first is the header, so it will be ignored.
with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # read header, and skip, as it is not needed in this code
    csv_header = next(csvreader)
    # now, read and deal with each row
    for row in csvreader:
        months=months+1 # let's count months
        date=row[0] # let's get the date
        pl=int(row[1]) # let's get the PL
        total= total + pl # let's get the total variation.
        if pl > 0: # dealing with the greatest increase
            if pl > greater:
                greater=pl
                gdate = row[0]
        if pl < 0: # dealing with the greatest decrease
            if pl < lower:
                lower = pl
                ldate= row[0]

# Presenting results on terminal screen
print("")
print("Analysis Results")
print("")
print("Total Months:" + str(months))
print("Total: $" + str(total))
print("Average Change: " + str(total / months))
print("Greatest Increase in Profits: " + gdate + " $" + str(greater))
print("Greatest Decrease in Profits: " + ldate +  " $" +str(lower))
# saving values to a file
with open(output_file, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    # writing the output
    csvwriter.writerow(["ANALYSIS RESULTS", ''])
    csvwriter.writerow(["TOTAL MONTHS", str(months)])
    csvwriter.writerow(["TOTAL $", str(total)])
    csvwriter.writerow(["AVERAGE CHANGE", str(total/months)])
    csvwriter.writerow(["GREATEST INCREASE IN PROFITS (" +gdate+ ")", str(greater)])
    csvwriter.writerow(["GREATEST DECREASE IN PROFITS (" +ldate+ ")", str(lower)])
    
# And that's all for the day!




