import os 
import csv 

#Collecting Data From Resources Folder 
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

date = []
profit = []
changes = []

with open(budget_data_csv, 'r') as csvfile: 

    csvreader = csv.reader(csvfile, delimiter = ',') 
    header = next(csvreader) 

    for row in csvreader:

        date.append(row[0])

        profit.append(row[1])


numofmonths = len(date)
print(f"Total Months: {numofmonths}")

#https://stackoverflow.com/questions/7368789/convert-all-strings-in-a-list-to-int
profit = [int(i) for i in profit]

#https://www.geeksforgeeks.org/python-program-to-find-sum-of-elements-in-list/
totalprofit = 0 
difference = 0 
for row in range(0,len(profit)):
    totalprofit = totalprofit + profit[row]
    if row != len(profit) - 1:
        difference = profit[row + 1] - profit[row]
        changes.append(difference)
    else:
        break

print(f"Total: ${totalprofit}")

average = sum(changes) / len(changes)
average = round(average, 2)
print(f"Average Changes: ${average}")


   

print("pass")
