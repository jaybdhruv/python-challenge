#import dependencies
import os
import csv

#select a path for a CSV file in Resources folder to read
election_csv = os.path.join("Resources","election_data.csv")

#Declaring variables
total_votes = 0

khan = 0
correy = 0
li = 0
otooley = 0

percent_khan = 0
percent_correy = 0
percent_li = 0
percent_otooley = 0

#Reading CSV file
with open(election_csv) as election_file:
    csvreader = csv.reader(election_file, delimiter = ',')

    #skipping header row
    header = next(csvreader)

    #Looping through rows of CSV file
    for row in csvreader:

        #Calculating total votes 
        total_votes += 1
        
        #If loop to calculate total votes for each candidates
        #increment candidate variable if it is equal to row value
        if row[2] == "Khan":
            khan += 1
        elif row[2] == "Correy":
            correy += 1
        elif row[2] == "Li":
            li+= 1
        elif row[2] == "O'Tooley":
            otooley += 1

    #Calculating percentage votes for each candidate
    #Formatting number into percentage
    percent_khan = "{:.3%}".format(khan/total_votes)
    percent_correy = "{:.3%}".format(correy/total_votes)
    percent_li = "{:.3%}".format(li/total_votes)
    percent_otooley = "{:.3%}".format(otooley/total_votes)

    #Dictionary to define key-value pair of total votes for each candidate with their name
    candidate = {khan:"Khan",correy:"Correy",li:"Li",otooley:"O'Tooley"}
    
    #using max() function to find the highest value of key in the dictionary
    #using get() function to get value for the highest key in a variable
    #this will determine our winner
    winner = candidate.get(max(candidate))

#Entering print statements into a variable 
election_result = ("Election Results\n"
                    "----------------------\n"
                    "Total Votes: {total_votes}\n"
                    "----------------------\n"
                    f"Khan: {percent_khan} ({khan})\n"
                    f"Correy: {percent_correy} ({correy})\n"
                    f"Li: {percent_li} ({li})\n"
                    f"O'Tooley: {percent_otooley} ({otooley})\n"
                    "----------------------\n"
                    f"Winner: {winner}\n"
                    "----------------------")

#printing result on terminal
print(election_result)

#select a path to store output in an Analysis folder
output_path = os.path.join("Analysis","PyPoll_Analysis.txt")

#Writing output in a Text file
with open(output_path, "w") as txtfile:
    txtfile.write(election_result)
