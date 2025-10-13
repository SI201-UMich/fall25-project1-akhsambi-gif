# Name: Armana Akhsambiyeva 
# Student ID: 1442 9696
# uniqname: akhsambi 
# email: akhsambi@umich.edu
# Title of project: Calculating the Center and Variability of Penguin Data Set Measurements 

import csv 
import math 
#Function 1: Opening CSV File 

def read_penguin_data(filename):
    with open(filename, mode='r', newline='' ) as f:
        list_dicts = [] 
        csvReader = csv.reader(f)
        next(csvReader)
        for row in csvReader: 
            list_dicts.append(row)
    return list_dicts




