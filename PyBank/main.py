#import dependencies
import os
import csv

#select a path for a file in Resources folder
budget_csv = os.path.join('Resources','budget_data.csv')

total_months = 0
total_amount = 0

with open(budget_csv) as budget_file:
    csvreader = csv.reader(budget_file, delimiter = ',')

    header = next(csvreader)

    for row in csvreader:
        
        total_months += 1
        
        profit_loss = int(row[1])
        total_amount += profit_loss

print(total_amount)
print(total_months)

