import os 
import csv 
from decimal import *

election_data_csv = os.path.join('Resources', 'election_data.csv')

nameandvote = []

with open(election_data_csv, 'r') as csvfile: 

    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader) 

    for row in csvreader: 
        nameandvote.append(row[2])

numofvotes = len(nameandvote)
def percentage(totalvotes, allvotes):
    percent = (totalvotes / allvotes)*100
    percent = Decimal(percent)
    percent = round(percent, 3)
    return percent

totalkhan = nameandvote.count("Khan")
percentkhan = percentage(totalkhan, numofvotes)

totalcorrey = nameandvote.count("Correy")
percentcorrey = percentage(totalcorrey, numofvotes)

totalli = nameandvote.count("Li")
percentli = percentage(totalli, numofvotes)

totalotooley = nameandvote.count("O'Tooley")
percentotooley = percentage(totalotooley, numofvotes) 

nameofcandidate = ["Khan","Correy","Li","O'Tooley"]
percentvotes = [percentkhan,percentcorrey,percentli,percentotooley]
eachtotalcandidatevotes = [totalkhan,totalcorrey,totalli,totalotooley]

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
for row in range(0,len(nameofcandidate)):
    print (f"{nameofcandidate[row]}: {percentvotes[row]}% ({eachtotalcandidatevotes[row]})")
print ("----------------------") 
print ("-") 
print(f"Winner: {winner}")
print ("----------------------") 
print ("-") 
print("' ' '")

totalnumstring = " {}".format(numofvotes)
numofkhan = " {}% ({}) ".format(percentvotes[0],eachtotalcandidatevotes[0])
numofcorrey = " {}% ({}) ".format(percentvotes[1],eachtotalcandidatevotes[1])
numofli = " {}% ({}) ".format(percentvotes[2],eachtotalcandidatevotes[2])
numofotooley = " {}% ({}) ".format(percentvotes[3],eachtotalcandidatevotes[3])
winnerstring = " {}".format(winner) 

analysis = ["Total Votes: ", "Khan: ", "Correy: ", "Li: ", "O'Tooley: ", "Winner: "]
numresults = [totalnumstring, numofkhan, numofcorrey, numofli,numofotooley,winnerstring]

results = zip(analysis, numresults)

export_file = os.path.join('analysis','analysis.csv')

with open(export_file, "w", newline = '') as analysisfile:
    writer = csv.writer(analysisfile)

    writer.writerow(["Analyis"," Results"])
    
    writer.writerows(results)

