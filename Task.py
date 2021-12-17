import sys
import csv
from datetime import date,datetime

#open .csv file with csvreader
file = open(sys.argv[1])
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
dic={}

# Age calculate function
def Age(DOB):
    print(DOB)
    DOB = datetime.strptime(DOB,'%d-%m-%Y')
    print(DOB)
    today = date.today()
    Age = today.year - DOB.year
    return Age

#concatinate First & Last Name
for record in csvreader:
    record.append([record[0]+' '+record[1]])
    print(record[2])
    # store First_Name + Last_rname As Key & Age As Value
    dic[record[0]+' '+record[1]] = Age(record[2])
print(dic)

#Write data into New_Patient.csv file
with open('New_Patient.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in dic.items():
       writer.writerow([key, value])


#Read _New_Patient.csv file
with open('New_Patient.csv','r')as file:
   file=csv.reader(file)
   for record in file:
       print(record)

file.close()
