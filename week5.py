import csv
import pandas
import statistics

#alternative way of looping thru file
#dont have to know what length or number of records
#dont have to close the file
tottemp = 0
with open("myfile3.csv", "r", newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader, None)
    print("Header with:", header)
    for row in csvreader:
        print(row[0])
        print(row[1])
        tottemp = tottemp + int(row[0])
        #add code to accum average here
        #add code to count the records here