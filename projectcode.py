# Name: Armana Akhsambiyeva 
# Student ID: 1442 9696
# uniqname: akhsambi 
# email: akhsambi@umich.edu
# Title of project: Calculating the Center and Variability of Penguin Data Set Measurements 
#GenAI use: 
# 1. Used Gen AI to explain how to use and structure decimal places in unit test cases using places=2 to round the resulting calculation from sample of csv (like the mean and variance to the hundreth decimal place) and assertAlmostEqual
# 2. used AI to debug when I assigned the wrong f string variable that did not match the key names I gave to bill_length dict on line 65 (used center_val instead of bill_length_mean in write to text file on line 95)
# not GenAI but used a website to look up different assert statements viable for unittests (link: https://understandingdata.com/posts/list-of-python-assert-statements-for-unit-tests/)
# referred to the runestone lesson 20 to remind myself of correct unit test import and structure, used GenAI for simplified outline of unittest import and class creation (not done for the test functions, I basically asked for an easier format outline but in the end it ended up being the same as the last code block practice in lesson 20.8 on runestone) 
#used GenAI to clean up the code and check that each function made sense after writing - explained in video
#overall, I used GenAI relatively often for this project

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


#Test Cases with Unit tests 

import unittest
from projectcode import (
    read_penguin_data,
    center_mean,
    variability_variance,
    standard_deviation,
    bill_length_summary,
    bill_depth_summary,
    flipper_length_summary,
    write_to_txt) 

class TestPenguinFunctions(unittest.TestCase):
    def test_read_penguin_data_type(self): #test case 1 
        data = read_penguin_data("penguins 3.csv")
        self.assertIsInstance(data, list)
        self.assertIsInstance(data[0], dict)
    def test_read_penguin_data_not_empty(self): #test case 2 
        data = read_penguin_data("penguins 3.csv")
        self.assertTrue(len(data) > 0)
    def test_read_penguin_data_empty(self):  # edge test 1
        with open("test_header_only.csv", "w") as f:
            f.write("species,bill_length_mm,bill_depth_mm,flipper_length_mm\n")
            data = read_penguin_data("test_header_only.csv")
            self.assertEqual(len(data), 0)  
    def test_read_penguin_data_with_NA(self):  # edge test 2
        with open("test_with_NA.csv", "w") as f:
            f.write("species,bill_length_mm,bill_depth_mm,flipper_length_mm\n")
            f.write("Adelie,NA,18.0,190\n")
            f.write("Adelie,41.0,NA,191\n")
        data = read_penguin_data("test_with_NA.csv")
        self.assertIsInstance(data, list)
        self.assertIn("bill_length_mm", data[0]) 


class TestCenterMean(unittest.TestCase):
    def test_center_mean(self): #test case 1 
        data = [{"bill_length_mm": "40.0"}, {"bill_length_mm": "42.0"}, {"bill_length_mm": "38.0"}]
        self.assertEqual(center_mean(data, "bill_length_mm"), 40.0)
    def test_center_mean_decimal(self): #test case 2 
        data = [{"bill_length_mm": "39.5"}, {"bill_length_mm": "40.5"}, {"bill_length_mm": "41.0"}]
        self.assertAlmostEqual(center_mean(data, "bill_length_mm"), 40.33, places=2)
    def test_center_mean_with_NA(self): #edge test 1 
        data = [{"bill_length_mm": "40.0"}, {"bill_length_mm": "NA"}, {"bill_length_mm": "42.0"}]
        self.assertEqual(center_mean(data, "bill_length_mm"), 41.0)
    def test_center_mean_one_value(self): #edge test 2 
        data = [{"bill_length_mm": "NA"}, {"bill_length_mm": "44.0"}]
        self.assertEqual(center_mean(data, "bill_length_mm"), 44.0)

class TestVariability_Variance(unittest.TestCase): 
    def test_variability_variance(self): #test case 1 
        data = [{"bill_length_mm": "40.0"}, {"bill_length_mm": "42.0"}, {"bill_length_mm": "38.0"}]
        self.assertAlmostEqual(variability_variance(data, "bill_length_mm"), 4.0, places=2)
    def test_variance_decimal(self): #test case 2 
        data = [{"bill_length_mm": "39.5"}, {"bill_length_mm": "40.5"}, {"bill_length_mm": "41.5"}]
        self.assertAlmostEqual(variability_variance(data, "bill_length_mm"), 1.0, places=2)
    def test_variance_all_equal(self): #edge test 1 
        data = [{"bill_length_mm": "40.0"}, {"bill_length_mm": "40.0"}, {"bill_length_mm": "40.0"}]
        self.assertEqual(variability_variance(data, "bill_length_mm"), 0.0)
    def test_variance_with_NA(self): #edge test 2 
        data = [{"bill_length_mm": "40.0"}, {"bill_length_mm": "NA"}, {"bill_length_mm": "42.0"}]
        self.assertAlmostEqual(variability_variance(data, "bill_length_mm"), 2.0, places=2)

class TestStandard_Deviation(unittest.TestCase): 
    def test_sd(self): #test case 1 
        data = [{"bill_length_mm": "40.0"}, {"bill_length_mm": "42.0"}, {"bill_length_mm": "38.0"}]
        self.assertAlmostEqual(standard_deviation(data, "bill_length_mm"), 2.0, places=2)
    def test_sd_decimal(self): #test case 2
        data = [{"bill_length_mm": "39.5"}, {"bill_length_mm": "40.5"}, {"bill_length_mm": "41.5"}]
        self.assertAlmostEqual(standard_deviation(data, "bill_length_mm"), 1.0, places=2)
    def test_sd_all_equal(self): #edge test 1 
        data = [{"bill_length_mm": "40.0"}, {"bill_length_mm": "40.0"}, {"bill_length_mm": "40.0"}]
        self.assertEqual(standard_deviation(data, "bill_length_mm"), 0.0)
    def test_sd_with_NA(self): #edge test 2 
        data = [{"bill_length_mm": "40.0"}, {"bill_length_mm": "NA"}, {"bill_length_mm": "42.0"}]
        self.assertAlmostEqual(standard_deviation(data, "bill_length_mm"), 1.41, places=2)

class TestBillLengthSummary(unittest.TestCase):
    def test_bill_length_summary_keys(self): #test case 1 
        data = [{"bill_length_mm": "40.0"}, {"bill_length_mm": "42.0"}, {"bill_length_mm": "38.0"}]
        result = bill_length_summary(data)
        self.assertIn("bill_length_mean", result)
        self.assertIn("bill_length_variance", result)
        self.assertIn("bill_length_sd", result)
    def test_bill_length_mean_value(self): #test case 2 
        data = [{"bill_length_mm": "39.0"}, {"bill_length_mm": "41.0"}]
        result = bill_length_summary(data)
        self.assertEqual(result["bill_length_mean"], 40.0)
    def test_bill_length_summary_with_NA(self): #edge test 1 
        data = [{"bill_length_mm": "NA"}, {"bill_length_mm": "42.0"}, {"bill_length_mm": "38.0"}]
        result = bill_length_summary(data)
        self.assertAlmostEqual(result["bill_length_mean"], 40.0, places=1)
    def test_bill_length_all_equal(self): #edge test 2 
        data = [{"bill_length_mm": "40.0"}, {"bill_length_mm": "40.0"}, {"bill_length_mm": "40.0"}]
        result = bill_length_summary(data)
        self.assertEqual(result["bill_length_variance"], 0.0)
        self.assertEqual(result["bill_length_sd"], 0.0)

class TestBillDepthSummary(unittest.TestCase):
    def test_bill_depth_summary_keys(self): #test case 1 
        data = [{"bill_depth_mm": "18.0"}, {"bill_depth_mm": "19.0"}, {"bill_depth_mm": "17.0"}]
        result = bill_depth_summary(data)
        self.assertIn("bill_depth_mean", result)
    def test_bill_depth_mean_value(self): #test case 2 
        data = [{"bill_depth_mm": "18.0"}, {"bill_depth_mm": "20.0"}]
        result = bill_depth_summary(data)
        self.assertEqual(result["bill_depth_mean"], 19.0)
    def test_bill_depth_summary_with_NA(self): #edge test 1 
        data = [{"bill_depth_mm": "NA"}, {"bill_depth_mm": "19.0"}, {"bill_depth_mm": "17.0"}]
        result = bill_depth_summary(data)
        self.assertAlmostEqual(result["bill_depth_mean"], 18.0, places=1)
    def test_bill_length_all_equal(self): #edge test 2 
        data = [{"bill_depth_mm": "18.0"}, {"bill_depth_mm": "18.0"}, {"bill_depth_mm": "18.0"}]
        result = bill_depth_summary(data)
        self.assertEqual(result["bill_depth_sd"], 0.0)

class TestFlipperLengthSummary(unittest.TestCase):
    def test_flipper_contains_keys(self): #test case 1 
        data = [{"flipper_length_mm": "180.0"}, {"flipper_length_mm": "190.0"}, {"flipper_length_mm": "200.0"}]
        result = flipper_length_summary(data)
        self.assertIn("flipper_length_mean", result)
    def test_flipper_mean_value(self): #test case 2 
        data = [{"flipper_length_mm": "180.0"}, {"flipper_length_mm": "200.0"}]
        result = flipper_length_summary(data)
        self.assertEqual(result["flipper_length_mean"], 190.0)
    def test_flipper_with_NA(self): #edge test 1 
        data = [{"flipper_length_mm": "NA"}, {"flipper_length_mm": "190.0"}, {"flipper_length_mm": "200.0"}]
        result = flipper_length_summary(data)
        self.assertAlmostEqual(result["flipper_length_mean"], 195.0, places=1)
    def test_flipper_all_same(self): #edge test2 
        data = [{"flipper_length_mm": "190.0"}, {"flipper_length_mm": "190.0"}, {"flipper_length_mm": "190.0"}]
        result = flipper_length_summary(data)
        self.assertEqual(result["flipper_length_sd"], 0.0)

class TestWriteToText(unittest.TestCase):
    def test_write_file(self): #test case 1 
        bill = {"bill_length_mean": 40, "bill_length_variance": 4, "bill_length_sd": 2}
        depth = {"bill_depth_mean": 18, "bill_depth_variance": 2, "bill_depth_sd": 1.4}
        flipper = {"flipper_length_mean": 190, "flipper_length_variance": 100, "flipper_length_sd": 10}
        write_to_txt(bill, depth, flipper)
        with open("penguin_summary.txt", mode="r") as f:
            content = f.read()
        self.assertIn("Penguin Data Set Center and Variability Summary", content)
    def test_write_contains_sections(self): #test case 2
        bill = {"bill_length_mean": 40, "bill_length_variance": 4, "bill_length_sd": 2}
        depth = {"bill_depth_mean": 18, "bill_depth_variance": 2, "bill_depth_sd": 1.4}
        flipper = {"flipper_length_mean": 190, "flipper_length_variance": 100, "flipper_length_sd": 10}
        write_to_txt(bill, depth, flipper)
        with open("penguin_summary.txt", mode="r") as f:
            content = f.read()
        self.assertIn("Bill Length", content)
        self.assertIn("Bill Depth", content)
        self.assertIn("Flipper Length", content)
    def test_write_returns_none(self): #edge test 1 
        bill = {"bill_length_mean": 40, "bill_length_variance": 4, "bill_length_sd": 2}
        depth = {"bill_depth_mean": 18, "bill_depth_variance": 2, "bill_depth_sd": 1.4}
        flipper = {"flipper_length_mean": 190, "flipper_length_variance": 100, "flipper_length_sd": 10}
        result = write_to_txt(bill, depth, flipper)
        self.assertIsNone(result)
    def test_write_overwrites(self): #edge test 2 
        bill1 = {"bill_length_mean": 40, "bill_length_variance": 4, "bill_length_sd": 2}
        depth1 = {"bill_depth_mean": 18, "bill_depth_variance": 2, "bill_depth_sd": 1.4}
        flipper1 = {"flipper_length_mean": 190, "flipper_length_variance": 100, "flipper_length_sd": 10}
        write_to_txt(bill1, depth1, flipper1)
        bill2 = {"bill_length_mean": 44, "bill_length_variance": 9, "bill_length_sd": 3}
        depth2 = {"bill_depth_mean": 17, "bill_depth_variance": 1, "bill_depth_sd": 1}
        flipper2 = {"flipper_length_mean": 200, "flipper_length_variance": 64, "flipper_length_sd": 8}
        write_to_txt(bill2, depth2, flipper2)
        with open("penguin_summary.txt", "r") as f:
            content = f.read()
        self.assertIn("bill_length_mean: 44", content)

class TestMainFunction(unittest.TestCase):
    def test_main_runs(self):  # test case 1 
        main()
        self.assertTrue(True) 
    def test_main_creates_text(self):  #test case 2
        main()
        f = open("penguin_summary.txt", mode="r")
        content = f.read()
        f.close()
        self.assertIn("Penguin Data Set Center and Variability Summary", content)
    def test_main_includes_sections(self):  #edge test1
        main()
        f = open("penguin_summary.txt", "r")
        text = f.read()
        f.close()
        self.assertIn("Bill Length", text)
        self.assertIn("Bill Depth", text)
        self.assertIn("Flipper Length", text)
    def test_main_creates_mean_values(self):  # edge test 2
        main()
        f = open("penguin_summary.txt", "r")
        text = f.read()
        f.close()
        self.assertIn("mean", text)
