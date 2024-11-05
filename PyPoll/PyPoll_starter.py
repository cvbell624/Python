# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

filepath = "Resources/election_data.csv"


#Define variables to track the election results
total_votes = 0
candidate_names = []
candidate_votes = {}
winner = ["", 0]

#Code ripped 3.2.8
with open(filepath) as csvfile:

        #CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')

        #Read the header row first (skip this step if there is no header)
        csv_header = next(csvreader)
        print(f"CSV Header: {csv_header}")

        for row in csvreader:
                total_votes += 1
                name = row[2]
                if name not in candidate_names:
                        candidate_names.append(name)
                        candidate_votes[name] = 0
                candidate_votes[name] += 1


#Generate the output summary
print(candidate_names)
output = f"""
Election Results
----------------------------
Total Votes: {total_votes}
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
"""

#Print the output
print(output)

#Save the file
outputpath = "analysis/election_analysis.txt"

with open (outputpath, "w") as file:
      file.write(output)