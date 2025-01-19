import csv

with open("stocks.csv") as file:
    csv_reader = csv.DictReader(file, delimiter=",")
    #print(list(csv_reader))
    for i in csv_reader:
        print(i)
        print(i["ProductName"])