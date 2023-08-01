"""
import glob

myfiles = glob.glob(r"D:\pythonProjects\courseProjects\thePythonMegaCourse\ToDoList\files\*.txt")

for file in myfiles:
    print(file)

import csv

with open(r"D:\pythonProjects\courseProjects\thePythonMegaCourse\ToDoList\files\weather.csv", 'r') as fh:
    data = list(csv.reader(fh))

print(data)

city = input("Enter a city: ")

for row in data:
    if row[0] == city:
        print(f"The temperature is: {row[1]}")

import shutil

shutil.make_archive("zip_file", "zip", r"D:\pythonProjects\courseProjects\thePythonMegaCourse\ToDoList\files")
"""

import webbrowser

user_term = input("Enter a search term: ")
query_term = "https://www.google.com/search?q=" + user_term
webbrowser.open(query_term)