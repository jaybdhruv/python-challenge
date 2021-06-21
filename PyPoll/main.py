#import dependencies
import os
import csv
#from collections import Counter

#select a path for a file in Resources folder
election_csv = os.path.join("Resources","election_data.csv")

total_votes = 0
#candidate = []

khan = 0
correy = 0
li = 0
otooley = 0
percent_khan = 0
percent_correy = 0
percent_li = 0
percent_otooley = 0

with open(election_csv) as election_file:
    csvreader = csv.reader(election_file, delimiter = ',')

    header = next(csvreader)

    for row in csvreader:

        total_votes += 1
        
        #candidate.append(row[2])

        #c = Counter(candidate)

        if row[2] == "Khan":
            khan += 1
        elif row[2] == "Correy":
            correy += 1
        elif row[2] == "Li":
            li+= 1
        elif row[2] == "O'Tooley":
            otooley += 1

percent_khan = round(((khan/total_votes)*100),2)
percent_correy = round(((correy/total_votes)*100),2)
percent_li = round(((li/total_votes)*100),2)
percent_otooley = round(((otooley/total_votes)*100),2)

candidate = {khan:"Khan",correy:"Correy",li:"Li",otooley:"O'Tooley"}

#candidate1 = {"Khan":khan,"Correy":correy,"Li":li,"O'Tooley":otooley}

#print(candidate)

#win = max(candidate)

winner = candidate.get(max(candidate))

election_result = (f"Election Results\n"
                    "----------------------\n"
                    f"Total Votes: {total_votes}\n"
                    "----------------------\n"
                    f"Khan: {percent_khan:.3f}% ({khan})\n"
                    f"Correy: {percent_correy:.3f}% ({correy})\n"
                    f"Li: {percent_li:.3f}% ({li})\n"
                    f"O'Tooley: {percent_otooley:.3f}% ({otooley})\n"
                    "----------------------\n"
                    f"Winner: {winner}\n"
                    "----------------------")

print(election_result)

output_path = os.path.join("Analysis","PyPoll_Analysis.txt")

with open(output_path, "w") as txtfile:
    txtfile.write(election_result)
