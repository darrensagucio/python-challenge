import os 
import csv 

#Collecting Data From Resources Folder 
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

date = []
profit = []

with open(budget_data_csv, 'r') as csvfile: 

    csvreader = csv.reader(csvfile, delimiter = ',') 
    header = next(csvreader) 

    for row in csvreader:

        date.append(row[0])

        profit.append(row[1])

numofmonths = len(date)

print(f"Total Months: {numofmonths}")
   

print("pass")
