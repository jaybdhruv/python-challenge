#import dependencies
import os
import csv

#select a path for a file in Resources folder
budget_csv = os.path.join('Resources','budget_data.csv')

total_months = 0
total_amount = 0
change = []
months = []

with open(budget_csv) as budget_file:
    csvreader = csv.reader(budget_file, delimiter = ',')

    header = next(csvreader)
    
    first_row = next(csvreader)
    total_months += 1
    total_amount = int(first_row[1])

    previous_amount = int(first_row[1])

    for row in csvreader:
        
        total_months += 1
        
        total_amount += int(row[1])

        change.append(int(row[1])-previous_amount)
        months.append(row[0])

        previous_amount = int(row[1])

average = round(sum(change)/len(change),2)

greatest_increase = max(change)
greatest_decrease = min(change)

index_max = change.index(max(change))

print(index_max)




print(greatest_decrease)
print(greatest_increase)
print("${:,.2f}".format(average))       
print(total_amount)
print(total_months)