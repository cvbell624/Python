# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

filepath = "Resources/budget_data.csv"

#Define variables to track the financial data
total_months = 0
total_net = 0

last_month_profit = 0
current_month_profit = 0
total_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999]

#Code ripped 3.2.8
with open(filepath) as csvfile:

        #CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')

        #Read the header row first (skip this step if there is no header)
        csv_header = next(csvreader)
        #print(f"CSV Header: [csv_header]")

        #Read each row of data after the header
        for row in csvreader:
                #print(row)
                total_months += 1
                total_net += int(row[1])

                #Check if first row - skip first row
                if total_months == 1:
                    last_month_profit = int(row[1])
                else:
                    #get change
                    current_month_profit = int(row[1])
                    change = current_month_profit - last_month_profit
                    total_change += change
                    if change > greatest_increase [1]: 
                          greatest_increase[1] = change
                          greatest_increase[0] = row [0]
                    if change < greatest_decrease [1]: 
                          greatest_decrease[1] = change
                          greatest_decrease[0] = row [0]


                    #reset
                    last_month_profit = current_month_profit

#Generate the output summary
output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_net}
Average Change: ${total_change/ (total_months - 1):.2f}
Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})
Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})
"""



#Print the output
print(output)

#Save the file
outputpath = "analysis/budget_analysis.txt"

with open (outputpath, "w") as file:
      file.write(output)