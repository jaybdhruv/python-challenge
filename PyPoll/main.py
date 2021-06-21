#import dependencies
import os
import csv

#select a path for a file in Resources folder
election_csv = os.path.join('Resources','election_data.csv')

total_votes = 0

abc = []

votes_khan = 0
votes_correy = 0
votes_li = 0
votes_otooley = 0

percent_khan = 0
percent_correy = 0
percent_li = 0
percent_otooley = 0

with open(election_csv) as election_file:
    csvreader = csv.reader(election_file, delimiter = ',')

    header = next(csvreader)

    for row in csvreader:

        abc = row[0] 
        total_votes += 1

        if row[2] == "Khan":
            votes_khan += 1
        elif row[2] == "Correy":
            votes_correy += 1
        elif row[2] == "Li":
            votes_li += 1
        elif row[2] == "O'Tooley":
            votes_otooley += 1
        
    percent_khan = round(((votes_khan/total_votes)*100),2) 
    percent_correy = round(((votes_correy/total_votes)*100),2)
    percent_li = (votes_li/total_votes)*100
    percent_otooley = (votes_otooley/total_votes)*100

print(abc.count())

'''print(f"Khan: {votes_khan} % {percent_khan}")
print(f"Correy: {votes_correy} % {percent_correy}")
print(f"Li: {votes_li} % {percent_li}")
print(f"O'Tooley: {votes_otooley} % {percent_otooley}")

print(total_votes)'''
