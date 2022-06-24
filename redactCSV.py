import csv
import os
import string
import random

filestoremove = []
for filename in os.listdir():
    if ".csv" in filename and "redacted" not in filename:
        print("\n" + filename )
        filestoremove.append(filename)

for FILE in filestoremove:
    csvfile = open(FILE, "r")
    csvReader = csv.reader(csvfile, delimiter=',')
    finishList = []
    finishList.append(next(csvReader)) 
    for row in csvReader:
        for count,cell in enumerate(row):
            new_string = cell.translate(str.maketrans('', '', string.punctuation))
            if new_string.isdigit():
                row[count] = random.randint(0,1000) 
        finishList.append(row)
        
    csvfile.close()
    csvfile = open("redacted_{}".format(FILE), "w")
    csvWriter = csv.writer(csvfile, delimiter = ",")
    csvWriter.writerows(finishList)