'''
We can read csv in Python by following two way.
csv Module: By using csv module we can read or write tabular information in CSV file format.
pandas Library: The pandas library is one of the open-source Python libraries that provide high-performance, convenient data structures and data analysis tools and techniques for Python programming. 

'''

import csv

import pandas

# opening the CSV file
with open('C:\\Temp\\team.csv', mode ='r') as file:
    
  file_1 = csv.reader(file)

  for line in file_1:
      print (line)

# reading the CSV file
  csvFile = csv.DictReader(file)
 
       # displaying the contents of the CSV file
  print(csvFile)

  for lines in csvFile:
         # print(lines)

# reading the CSV file
    csvFile_1 = pandas.read_csv('C:\\Temp\\team.csv')
 
  # displaying the contents of the CSV file
    print(csvFile_1)

