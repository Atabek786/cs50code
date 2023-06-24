import csv

books = []

with open("books.csv") as file:
    text = file.read()
    print(text)
