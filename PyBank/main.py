import os
import csv

budget_csv = os.path.join('Resources','budget_data.csv')

total_months = 0

with open(budget_csv) as budget_file:
    csvreader = csv.reader(budget_file, delimiter = ',')

    header = next(csvreader)

    for row in csvreader:
        
        total_months += 1

        





print(total_months)

