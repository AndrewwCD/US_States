import ssl
import csv
import requests
import pandas as pd



csvFile = open("usa.states.txt","r")
csvText = csv.reader(csvFile)

newFile = open("usa_states_and_capitals.txt","w")
statesAndCapitals = csv.writer(newFile, lineterminator = '\n')
header = "State","Capital"
statesAndCapitals.writerow(header)

table = pd.read_html("https://en.wikipedia.org/wiki/List_of_capitals_in_the_United_States",header=0)
table = table[1]

for line in csvText:
    state = (line[0])
    row = table.loc[table['State'] == state]
    capital = row["Capital"].to_string(index=False)
    stateAndCapital = [state,capital]
    statesAndCapitals.writerow(stateAndCapital)
    print(stateAndCapital)
