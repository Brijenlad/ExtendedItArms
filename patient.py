import pandas as pd
import numpy as np
from datetime import date
import sys
from dateutil.parser import parse
#read csv file
def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try:
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False


todays_date = date.today() #todays date in yyyy-mm-dd
print(todays_date)
dataFrame = pd.read_csv("patient.csv") #read csv and data frame created
print(dataFrame) #show data
dataFrame2 = pd.DataFrame() #created new dataframe
dataFrame2["Patient_Name"] = dataFrame["Patient_First_Name"]+" "+ dataFrame["Patient_Last_Name"] #conactenated 2 columns from original dataframe
# and data put into new data frame 2
x = dataFrame["DOB"] #extracted DOB column values
lst=[] #created empty list

for i in x: #for each date
    if pd.isna(i) or not is_date(i): #check if date is Null/NAN or some unknown String
        lst.append("No DOB") #then show value "no dob"
    else: #else subtract dates and generate age
        lst.append(todays_date.year-int(i[6:10])) #extracted age

dataFrame2["Patient_Age"]=pd.DataFrame(lst) #put list into dataframe2 as column
print(dataFrame2) #show data frame 2
new_column_names = ['Patient_Name', 'Patient_Age'] #new column names
dataFrame2.to_csv('New_Patient.csv', index=False, header=new_column_names) # write into new csv file
