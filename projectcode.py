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
        csvReader = csv.DictReader(f)
        next(csvReader)
        for row in csvReader: 
            list_dicts.append(row)
    return list_dicts

#Second function, arthmetic mean calculation (measure of center)

def center_mean(list_dicts, quant_var): 
    total = 0 
    count = 0 
    for row in list_dicts: 
        if row[quant_var] != 'NA': 
            total += float(row[quant_var])
            count += 1 
        else: 
            continue 
    mean = total/count 
    return mean 

#Third function, variance calculation that calls on the mean computation function 2: variance equation for reference: sum(xi - mean)^2/(sample size n - 1)

def variability_variance(list_dicts, quant_var): 
    mean = center_mean(list_dicts, quant_var)
    total_square = 0 
    count = 0 
    for row in list_dicts: 
        if row[quant_var] != 'NA': 
            value = float(row[quant_var])
            total_square += (value - mean) ** 2 #had difficulty here, I had trouble writing out the numerator part of the variance equation to code, difficult to visualize but managed to get done independently. 
            count += 1 
        else: 
            continue 
    variance_final = total_square / (count - 1) 
    return variance_final

#Fourth function, standard deviation calculation that calls on the variance computation function 3; equation for reference = square root of found variance 

def standard_deviation(list_dicts, quant_var): 
    variance = variability_variance(list_dicts, quant_var)
    standard_dev_result = math.sqrt(variance)
    return standard_dev_result

#Fifth function bill_length function with standard deviation, variance, and mean

def bill_length_summary(list_dicts):
    center_val = center_mean(list_dicts, "bill_length_mm")
    variance_val = variability_variance(list_dicts, "bill_length_mm" )
    standard_deviation_val = standard_deviation(list_dicts, "bill_length_mm")
    bill_length_dict = {"bill_length_mean": center_val, "bill_length_variance": variance_val, "bill_length_sd": standard_deviation_val}  
    return bill_length_dict

#Sixth function bill_depth function with standard deviation, variance, and mean

def bill_depth_summary(list_dicts): 
    center_val = center_mean(list_dicts, "bill_depth_mm")
    variance_val = variability_variance(list_dicts, "bill_depth_mm" )
    standard_deviation_val = standard_deviation(list_dicts, "bill_depth_mm")
    bill_depth_dict = {"bill_depth_mean": center_val, "bill_depth_variance": variance_val, "bill_depth_sd": standard_deviation_val}  
    return bill_depth_dict

#Seventh function flipper_length function with standard deviation, variance, and mean

def flipper_length_summary(list_dicts): 
    center_val = center_mean(list_dicts, "flipper_length_mm")
    variance_val = variability_variance(list_dicts, "flipper_length_mm")
    standard_deviation_val = standard_deviation(list_dicts, "flipper_length_mm")
    flipper_length_dict = {"flipper_length_mean": center_val, "flipper_length_variance": variance_val, "flipper_length_sd": standard_deviation_val}  
    return flipper_length_dict

#Eigth function writing dict results from functions 5-7 into txt file 

def write_to_txt(bill_length_dict, bill_depth_dict, flipper_length_dict):
    with open('penguin_summary.txt', mode='w') as f: 
        f.write('Penguin Data Set Center and Variability Summary\n')
        f.write('\n')
        f.write('Bill Length (in millimeters) Mean, Variance, Standard Deviation \n') 
        for key, value in bill_length_dict.items(): 
            f.write(f'{key}: {value} \n')
        f.write(f"Based on the data collected from a sample size of n = 344 penguins from the penguins.csv data set, the mean of {bill_length_dict['bill_length_mean']} is the center of the distribution. the {bill_length_dict['bill_length_variance']} is the measure of average spread, meaning the mm values from the Bill length mm column are spread around the center {bill_length_dict['bill_length_mean']} by approximately {bill_length_dict['bill_length_sd']}\n")
        
        f.write('\n')
        f.write('Bill Depth (in millimeters) Mean, Variance, Standard Deviation \n') 
        for key, value in bill_depth_dict.items(): 
            f.write(f'{key}: {value} \n')
        f.write(f"Based on the data collected from a sample size of n = 344 penguins from the penguins.csv data set, the mean of {bill_depth_dict['bill_depth_mean']} is the center of the distribution. the {bill_depth_dict['bill_depth_variance']} is the measure of average spread, meaning the mm values from the Bill Depth mm column are spread around the center {bill_depth_dict['bill_depth_mean']} by approximately {bill_depth_dict['bill_depth_sd']}\n")
        
        f.write('\n')
        f.write('Flipper Length (in millimeters) Mean, Variance, Standard Deviation \n') 
        for key, value in flipper_length_dict.items(): 
            f.write(f'{key}: {value} \n')
        f.write(f"Based on the data collected from a sample size of n = 344 penguins from the penguins.csv data set, the mean of {flipper_length_dict['flipper_length_mean']} is the center of the distribution. the {flipper_length_dict['flipper_length_variance']} is the measure of average spread, meaning the mm values from the Flipper Length mm column are spread around the center {flipper_length_dict['flipper_length_mean']} by approximately {flipper_length_dict['flipper_length_sd']}\n")



def main(): 
    filename = "penguins 3.csv"
    data = read_penguin_data(filename)
    bill_length_dict = bill_length_summary(data)
    bill_depth_dict = bill_depth_summary(data)
    flipper_length_dict = flipper_length_summary(data)
    write_to_txt(bill_length_dict, bill_depth_dict, flipper_length_dict)
if __name__ == "__main__":
    main()