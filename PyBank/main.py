import csv
import os

totalcounts = 0
totalpl = 0
previouspl = 0
diffpl = []
greatestinc = ["","0"]
greatestdec = ["","0"]
greatestincdiff = 0
greatestdecdiff = 0


# open the csv file
csv_path = os.path.join("Resources","budget_data.csv")
with open(csv_path) as budgetfile:
    budgetreader = csv.reader(budgetfile, delimiter=',')
    # store the header
    budgetheader = next(budgetreader)

    # read through rows
    for budget in budgetreader:
        # budget[0] is date
        # budget[1] is p/l
        totalcounts = totalcounts + 1
        # add all the p/l
        totalpl = totalpl + int(budget[1])
        # find the diff between current and the previous
        diff = int(budget[1]) - previouspl
        # store all the diff
        previouspl = int(budget[1]) 
        diffpl.append(diff)
        # keep the number when only if it is highest so far
        if diff > greatestincdiff:
            greatestinc = [budget[0], diff]
            greatestincdiff = diff
        #  keep the number when only if it is lowest so far
        if diff < greatestdecdiff:
            greatestdec = [budget[0], diff]
            greatestdecdiff = diff

# get rid of the first one, because it is not an actual diff
diffpl.pop(0)
avgdiff = sum(diffpl)/len(diffpl)

# confirm if we have all the info
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {totalcounts}")
print(f"Total: ${totalpl}")
print(f"Average Change: ${avgdiff:.2f}")
print(f"Greatest Increase in Profits: {greatestinc[0]} (${greatestinc[1]})")
print(f"Greatest Decrease in Profits: {greatestdec[0]} (${greatestdec[1]})")


allexportlines = []
allexportlines.append("Financial Analysis\n")
allexportlines.append("----------------------------\n")
allexportlines.append(f"Total Months: {totalcounts}\n")
allexportlines.append(f"Total: ${totalpl}\n")
allexportlines.append(f"Average Change: ${avgdiff:.2f}\n")
allexportlines.append(f"Greatest Increase in Profits: {greatestinc[0]} (${greatestinc[1]})\n")
allexportlines.append(f"Greatest Decrease in Profits: {greatestdec[0]} (${greatestdec[1]})\n")
export_path = os.path.join("analysis","result.txt")
with open(export_path, 'w') as exportfile:
    exportfile.writelines(allexportlines)








    