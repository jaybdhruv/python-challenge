#import dependencies
import os
import csv

#select a path for CSV file to read from Resources folder
election_csv = os.path.join("Resources","election_data.csv")

#declare variables, dictionary and list
total_votes = 0

khan = 0
correy = 0
li = 0
otooley = 0

candidate_votes = {}
percent = []

#read CSV file
with open(election_csv) as election_file:
    csvreader = csv.reader(election_file, delimiter = ',')

    #skip header row
    header = next(csvreader)

    #loop through rows of CSV file
    for row in csvreader:

        #calculate total votes by incrementing variable by 1 for each row 
        total_votes += 1
        
        #variable that will store candidate name for each iteration
        candidate = row[2]

        #use if loop to check if candidate name exists in candidate_votes dictionary
        #if it exist then increase count of votes for that candidate
        #candidate name and counter of votes acts as a key-value pair in this dictionary
        #initialize candidate counter if no value found in the dictionary
        if candidate in candidate_votes.keys():
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

#use for loop to search for candidate name in the key of the dictionary
#if it matches then calculate total number of votes and their percent win for each candidate
#use format percentage method to convert number into percentage with 3 decimal places and storing it in percent list
for candidate in candidate_votes.keys():
    if candidate == "Khan":
        khan = candidate_votes.get(candidate)
        percent.append("{:.3%}".format(khan/total_votes))
    elif candidate == "Correy":
        correy = candidate_votes.get(candidate)
        percent.append("{:.3%}".format(correy/total_votes))
    elif candidate == "Li":
        li = candidate_votes.get(candidate)
        percent.append("{:.3%}".format(li/total_votes))
    elif candidate == "O'Tooley":
        otooley = candidate_votes.get(candidate)
        percent.append("{:.3%}".format(otooley/total_votes))

#using max() and .get to find the key with highest value in dictionary
winner = max(candidate_votes, key=candidate_votes.get)

#enter print statements into a variable 
election_result = ("Election Results\n"
                    "----------------------\n"
                    f"Total Votes: {total_votes}\n"
                    "----------------------\n"
                    f"Khan: {percent[0]} ({khan})\n"
                    f"Correy: {percent[1]} ({correy})\n"
                    f"Li: {percent[2]} ({li})\n"
                    f"O'Tooley: {percent[3]} ({otooley})\n"
                    "----------------------\n"
                    f"Winner: {winner}\n"
                    "----------------------")

#printing result on terminal
print(election_result)

#select a path to store result in an Analysis folder as a text file
output_path = os.path.join("Analysis","PyPoll_Analysis.txt")

#write output in a text file
with open(output_path, "w") as txtfile:
    txtfile.write(election_result)