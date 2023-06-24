import csv

books = []

with open("books.csv") as file:
    file_reader = csv.reader(file)
    for row in file_reader:
        print(row[0])


