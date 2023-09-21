from bs4 import BeautifulSoup
import pandas as pd

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

list_items = soup.find_all('li')

#create a python list from all li html tags, gives a row for each li, [1] of each item in the list is everything that was between <li> and </li>
#soup = soup.findAll(name=["li"])

#separate each li in the soup object into columns
list_output = []
for li in list_items:
    company = li.find_all('span')
    row = [li.text for li in company]
    list_output.append(row)
df = pd.DataFrame(list_output, columns=["Company", "Role","C","D","E"])

#clean up some crap in the Company column
df["Company"] = df["Company"].str.replace(':','')
df["Company"] = df["Company"].str.strip()


with open('scrape.csv', 'w', newline='') as file:
    df.to_csv('scrape.csv')


