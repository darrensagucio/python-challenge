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

nameofcandiate = ["Khan","Correy","Li","O'Tooley"]
percentvotes = [percentkhan,percentcorrey,percentli,percentotooley]
eachtotalcandiatevotes = [totalkhan,totalcorrey,totalli,totalotooley]

highestvote = max(eachtotalcandiatevotes)

for row in range(0,len(eachtotalcandiatevotes)):
    if eachtotalcandiatevotes[row] != highestvote: 
        pass
    else: 
        winner = nameofcandiate[row]


print("' ' ' text")
print("Election Results")
print ("----------------------") 
print ("-") 
print (f"Total Votes: {numofvotes}")
print ("----------------------") 
print ("-") 
for row in range(0,len(nameofcandiate)):
    print (f"{nameofcandiate[row]}: {percentvotes[row]}% ({eachtotalcandiatevotes[row]})")
print ("----------------------") 
print ("-") 
print(f"Winner: {winner}")
print ("----------------------") 
print ("-") 
print("' ' '")