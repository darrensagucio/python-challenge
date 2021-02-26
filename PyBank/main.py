import os 
import csv 

# Collecting Data From Resources Folder 
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

# Making Lists
date = []
profit = []
changes = []

# Reads CSV
with open(budget_data_csv, 'r') as csvfile: 

    csvreader = csv.reader(csvfile, delimiter = ',') 
    # Skips Header
    header = next(csvreader) 

    for row in csvreader:

        date.append(row[0])

        profit.append(row[1])


# Converts String Into Ints In Lists (https://stackoverflow.com/questions/7368789/convert-all-strings-in-a-list-to-int)
profit = [int(i) for i in profit]

# Adding Total Profit (https://www.geeksforgeeks.org/python-program-to-find-sum-of-elements-in-list/)
totalprofit = 0 
difference = 0 
for row in range(0,len(profit)):
    totalprofit = totalprofit + profit[row]
    # Adding Last Row In The List
    if row != len(profit) - 1:
        difference = profit[row + 1] - profit[row]
        changes.append(difference)
    else:
        break

print(" ' ' ' text")
print("Finanical Analysis")
print("--------------------------")

# Total Months
numofmonths = len(date)
print(f"Total Months: {numofmonths}")

# Total Amount Of Profit
print(f"Total: ${totalprofit}")

# Average
average = sum(changes) / len(changes)
average = round(average, 2)
print(f"Average Change: ${average}")

# Finding Max and Min 
highestincrease = max(changes)
highestdecrease = min(changes)

for row in range(0,len(changes)):
    if changes[row] != highestincrease: 
        pass 
    else: 
        dateofincrease = date[row+1]
        break

for row in range(0,len(changes)):
    if changes[row] != highestdecrease: 
        pass 
    else: 
        dateofdecrease = date[row+1]
        break


print(f"Greatest Increase In Profits: {dateofincrease}  $({highestincrease})")
print(f"Greatest Decrease In Profits: {dateofdecrease}  $({highestdecrease})" )
print(" ' ' '")

# Formating String Variables (https://matthew-brett.github.io/teaching/string_formatting.html)
numofmonthsstring = " {}".format(numofmonths)
totalprofitstring = " ${}".format(totalprofit)
averagestring = " ${}".format(average)
increasestring = " {} ${}".format(dateofincrease, highestincrease) 
decreasestring = " {} ${}".format(dateofdecrease, highestdecrease) 

analysis = ["Total Months: ", "Total: ", "Average Change: ", 
            "Greatest Increase in Profits: ", "Greatest Decrease in Profits: "]
# Inserting String Variables To List
numresults =  [numofmonthsstring, totalprofitstring, averagestring, increasestring, decreasestring]

results = zip(analysis, numresults)

# Exporting To CSV
export_file = os.path.join('analysis','analysis.csv')

with open(export_file, "w", newline = '') as analysisfile:
    writer = csv.writer(analysisfile)

    writer.writerow(["Analysis", " Results"])

    writer.writerows(results)