import csv
import os

totalvote = 0
candidates = {}

file_path = os.path.join("Resources", "election_data.csv")
with open(file_path) as votefile:
    votereader = csv.reader(votefile, delimiter= ",")
    # get rid of the header
    next(votereader)

    # loop through the rows
    for vote in votereader:
        totalvote = totalvote + 1
        if vote[2] not in candidates:
            candidates[vote[2]] = 0
        candidates[vote[2]] = candidates[vote[2]] + 1

winner = ""
highestvotes = 0
print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalvote}")
print("-------------------------")
for name in candidates.keys():
    if candidates[name] > highestvotes:
        winner = name
        highestvotes = candidates[name]
    print(f"{name}: {candidates[name]/totalvote*100:.3f}% ({candidates[name]})")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

allexportlines = []

allexportlines.append("Election Results\n")
allexportlines.append("-------------------------\n")
allexportlines.append(f"Total Votes: {totalvote}\n")
allexportlines.append("-------------------------\n")
for name in candidates.keys():
    if candidates[name] > highestvotes:
        winner = name
        highestvotes = candidates[name]
    allexportlines.append(f"{name}: {candidates[name]/totalvote*100:.3f}% ({candidates[name]})\n")
allexportlines.append("-------------------------\n")
allexportlines.append(f"Winner: {winner}\n")
allexportlines.append("-------------------------\n")
export_path = os.path.join("analysis","result.txt")
with open(export_path, 'w') as exportfile:
    exportfile.writelines(allexportlines)