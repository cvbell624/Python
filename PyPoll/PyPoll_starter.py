# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

filepath = "/Users/cassidybell/DataBootCamp/Github_HW/03-Python/databootcamp_week3/PyPoll/Resources/election_data.csv"

#Define variables to track the election results
total_votes = 0

#Code ripped 3.2.8
with open(filepath) as csvfile:

        #CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')

        #Read the header row first (skip this step if there is no header)
        csv_header = next(csvreader)
        print(f"CSV Header: [csv_header]")