from bs4 import BeautifulSoup
import pandas as pd
import csv
import re

#
# Sample format of file I want to extract 
"""
<h2>Date1</h2>
    <ol>
        <li>Part1_of_row1: <a href="url_for_row1">Part2_of row1</li>
        .
        .
        .
        <li>Part1_of_rown: <a href="url_for_rown">Part2_of rown</li>
    </ol>
<h2>Date2</h2>
.
.
.

""" 


with open("myfile.html", "r") as og_file:
    page = str(og_file.read())

soup = BeautifulSoup(page, "html5lib")



#TODO find a way to retain the date from each H2
# possibly first run a findall on the H3?

#create a python list from all li html tags, gives a row for each li, [1] of each item in the list is everything that was between <li> and </li>
soup = soup.findAll(name=["li"])

list_output = []
for child in soup:
    for a in child:
        list_output.append(a)




with open('scrape.csv', 'w', newline='') as file:
    # Step 4: Using csv.writer to write the list to the CSV file
    writer = csv.writer(file)
    writer.writerows(list_output) 
    # Use writerow for single list


