#import dependencies
import os
import csv

#select a path for CSV file to read from Resource folder
budget_csv = os.path.join("Resources","budget_data.csv")

#declare variables and list
total_months = 0
total_amount = 0
change = []
change_months = []

#read CSV file
with open(budget_csv) as budget_file:
    csvreader = csv.reader(budget_file, delimiter = ',')

    #skip header
    header = next(csvreader)
    
    #enter first row and record its values for months and amount
    #first row is excluded from for loop as profit/loss change cannot be computed as previous values not found
    first_row = next(csvreader)
    total_months += 1
    total_amount = int(first_row[1])

    #hardcoding previous_amount with value of amount of first row
    previous_amount = int(first_row[1])

    ##loop through rows of CSV file
    for row in csvreader:
        
        #increment number of months for each iteration
        total_months += 1
        
        #add amount from profit/loss column for each iteration
        total_amount += int(row[1])

        #calculate difference in amounts and append each value in the change list
        change.append(int(row[1])-previous_amount)

        #append corresponding month in another list which will track months for each change
        change_months.append(row[0])
        
        #initialise value of previous amount to current row value for next iteration
        previous_amount = int(row[1])

#calculate average of the change using sum() and len() functions
average_change = round(sum(change)/len(change),2)

#find maximum value in the list for greatest increase in profits by using max() function
greatest_increase = max(change)

#find minimum value in the list for greatest decrease in profits by using min() function
greatest_decrease = min(change)

#using index() find the corresponding month for both greatest increase and greatest decrease
greatest_increase_month = change_months[change.index(greatest_increase)]
greatest_decrease_month = change_months[change.index(greatest_decrease)]

#enter print statements into a variable
financial_analysis = ("Financial Analysis\n"
                        "--------------------------\n"
                        f"Total Months: {total_months}\n"
                        f"Total: ${total_amount}\n"
                        f"Average Change: ${average_change}\n"
                        f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
                        f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

#print financial analysis on terminal
print(financial_analysis)

#select a path to store result in an Analysis folder as a text file
output_path = os.path.join("Analysis","PyBank Financial Analysis.txt")

##write output in a text file
with open(output_path, "w") as txtfile:
    txtfile.write(financial_analysis)