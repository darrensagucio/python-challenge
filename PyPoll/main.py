import os 
import csv 
# Imported Decimal Package
from decimal import *

election_data_csv = os.path.join('Resources', 'election_data.csv')

# Created List
nameandvote = []

# Read CSV File
with open(election_data_csv, 'r') as csvfile: 

    csvreader = csv.reader(csvfile, delimiter = ',')
    # Skips Header
    header = next(csvreader) 

    for row in csvreader: 
        nameandvote.append(row[2])

# Length Of List
numofvotes = len(nameandvote)

# Percentage Function 
def percentage(totalvotes, allvotes):
    percent = (totalvotes / allvotes)*100
    percent = Decimal(percent)
    percent = round(percent, 3)
    return percent

# Counts Unique Votes And Percentage Within The Election For Each Candidate
totalkhan = nameandvote.count("Khan")
percentkhan = percentage(totalkhan, numofvotes)

totalcorrey = nameandvote.count("Correy")
percentcorrey = percentage(totalcorrey, numofvotes)

totalli = nameandvote.count("Li")
percentli = percentage(totalli, numofvotes)

totalotooley = nameandvote.count("O'Tooley")
percentotooley = percentage(totalotooley, numofvotes) 

# Creating New Lists 
nameofcandidate = ["Khan","Correy","Li","O'Tooley"]
percentvotes = [percentkhan,percentcorrey,percentli,percentotooley]
eachtotalcandidatevotes = [totalkhan,totalcorrey,totalli,totalotooley]

# Finding Winner
highestvote = max(eachtotalcandidatevotes)

for row in range(0,len(eachtotalcandidatevotes)):
    if eachtotalcandidatevotes[row] != highestvote: 
        pass
    else: 
        winner = nameofcandidate[row]


print("' ' ' text")
print("Election Results")
print ("----------------------") 
print ("-") 
print (f"Total Votes: {numofvotes}")
print ("----------------------") 
print ("-") 
# For Loop To Print Candidate Name, Percentage, And Number Of Votes
for row in range(0,len(nameofcandidate)):
    print (f"{nameofcandidate[row]}: {percentvotes[row]}% ({eachtotalcandidatevotes[row]})")
print ("----------------------") 
print ("-") 
print(f"Winner: {winner}")
print ("----------------------") 
print ("-") 
print("' ' '")

# Creating String Variables (https://matthew-brett.github.io/teaching/string_formatting.html)
totalnumstring = " {}".format(numofvotes)
numofkhan = " {}% ({}) ".format(percentvotes[0],eachtotalcandidatevotes[0])
numofcorrey = " {}% ({}) ".format(percentvotes[1],eachtotalcandidatevotes[1])
numofli = " {}% ({}) ".format(percentvotes[2],eachtotalcandidatevotes[2])
numofotooley = " {}% ({}) ".format(percentvotes[3],eachtotalcandidatevotes[3])
winnerstring = " {}".format(winner) 

analysis = ["Total Votes: ", "Khan: ", "Correy: ", "Li: ", "O'Tooley: ", "Winner: "]
# Inserting String Variables Into Lists
numresults = [totalnumstring, numofkhan, numofcorrey, numofli,numofotooley,winnerstring]

results = zip(analysis, numresults)

# Exporting To A CSV File
export_file = os.path.join('analysis','analysis.csv')

with open(export_file, "w", newline = '') as analysisfile:
    writer = csv.writer(analysisfile)

    writer.writerow(["Analyis"," Results"])
    
    writer.writerows(results)