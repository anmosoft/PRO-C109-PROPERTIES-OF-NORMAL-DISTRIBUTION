import pandas as pd
import statistics
import csv
df = pd.read_csv("StudentsPerformance.csv")
math_scr_list = df["math score"].to_list()
reading_scr_list = df["reading score"].to_list()
writing_scr_list = df["writing score"].to_list()
#Mean for math_scr and reading_scr and writing_scr
math_scr_mean = statistics.mean(math_scr_list)
reading_scr_mean = statistics.mean(reading_scr_list)
writing_scr_mean = statistics.mean(writing_scr_list)
#Median for math_scr and reading_scr
math_scr_median = statistics.median(math_scr_list)
reading_scr_median = statistics.median(reading_scr_list)
writing_scr_median = statistics.median(writing_scr_list)
#Mode for math_scr and reading_scr
math_scr_mode = statistics.mode(math_scr_list)
reading_scr_mode = statistics.mode(reading_scr_list)
writing_scr_mode = statistics.mode(writing_scr_list)
#Printing mean, median and mode to validate
print("Mean, Median and Mode of math_scr is {}, {} and {} respectively".format(math_scr_mean, math_scr_median, math_scr_mode))
print("Mean, Median and Mode of reading_scr is {}, {} and {} respectively".format(reading_scr_mean, reading_scr_median, reading_scr_mode))
print("Mean, Median and Mode of writing_scr is {}, {} and {} respectively".format(writing_scr_mean, writing_scr_median, writing_scr_mode))
#Standard deviation for math_scr and reading_scr
math_scr_std_deviation = statistics.stdev(math_scr_list)
reading_scr_std_deviation = statistics.stdev(reading_scr_list)
writing_scr_std_deviation = statistics.stdev(writing_scr_list)
#1, 2 and 3 Standard Deviations for math_scr
math_scr_first_std_deviation_start, math_scr_first_std_deviation_end = math_scr_mean-math_scr_std_deviation, math_scr_mean+math_scr_std_deviation
math_scr_second_std_deviation_start, math_scr_second_std_deviation_end = math_scr_mean-(2*math_scr_std_deviation), math_scr_mean+(2*math_scr_std_deviation)
math_scr_third_std_deviation_start, math_scr_third_std_deviation_end = math_scr_mean-(3*math_scr_std_deviation), math_scr_mean+(3*math_scr_std_deviation)
#1, 2 and 3 Standard Deviations for reading_scr
reading_scr_first_std_deviation_start, reading_scr_first_std_deviation_end = reading_scr_mean-reading_scr_std_deviation, reading_scr_mean+reading_scr_std_deviation
reading_scr_second_std_deviation_start, reading_scr_second_std_deviation_end = reading_scr_mean-(2*reading_scr_std_deviation), reading_scr_mean+(2*reading_scr_std_deviation)
reading_scr_third_std_deviation_start, reading_scr_third_std_deviation_end = reading_scr_mean-(3*reading_scr_std_deviation), reading_scr_mean+(3*reading_scr_std_deviation)
#1, 2 and 3 Standard Deviations for writing_scr
writing_scr_first_std_deviation_start, writing_scr_first_std_deviation_end = writing_scr_mean-writing_scr_std_deviation, writing_scr_mean+writing_scr_std_deviation
writing_scr_second_std_deviation_start, writing_scr_second_std_deviation_end = writing_scr_mean-(2*writing_scr_std_deviation), writing_scr_mean+(2*writing_scr_std_deviation)
writing_scr_third_std_deviation_start, writing_scr_third_std_deviation_end = writing_scr_mean-(3*writing_scr_std_deviation), writing_scr_mean+(3*writing_scr_std_deviation)
#Percentage of data within 1, 2 and 3 Standard Deviations for math_scr
math_scr_list_of_data_within_1_std_deviation = [result for result in math_scr_list if result > math_scr_first_std_deviation_start and result < math_scr_first_std_deviation_end]
math_scr_list_of_data_within_2_std_deviation = [result for result in math_scr_list if result > math_scr_second_std_deviation_start and result < math_scr_second_std_deviation_end]
math_scr_list_of_data_within_3_std_deviation = [result for result in math_scr_list if result > math_scr_third_std_deviation_start and result < math_scr_third_std_deviation_end]
#Percentage of data within 1, 2 and 3 Standard Deviations for reading_scr
reading_scr_list_of_data_within_1_std_deviation = [result for result in reading_scr_list if result > reading_scr_first_std_deviation_start and result < reading_scr_first_std_deviation_end]
reading_scr_list_of_data_within_2_std_deviation = [result for result in reading_scr_list if result > reading_scr_second_std_deviation_start and result < reading_scr_second_std_deviation_end]
reading_scr_list_of_data_within_3_std_deviation = [result for result in reading_scr_list if result > reading_scr_third_std_deviation_start and result < reading_scr_third_std_deviation_end]
#Percentage of data within 1, 2 and 3 Standard Deviations for math_scr
writing_scr_list_of_data_within_1_std_deviation = [result for result in writing_scr_list if result > writing_scr_first_std_deviation_start and result < writing_scr_first_std_deviation_end]
writing_scr_list_of_data_within_2_std_deviation = [result for result in writing_scr_list if result > writing_scr_second_std_deviation_start and result < writing_scr_second_std_deviation_end]
writing_scr_list_of_data_within_3_std_deviation = [result for result in writing_scr_list if result > writing_scr_third_std_deviation_start and result < writing_scr_third_std_deviation_end]
#Printing data for math_scr and reading_scr (Standard Deviation)
print("{}% of data for math_scr lies within 1 standard deviation".format(len(math_scr_list_of_data_within_1_std_deviation)*100.0/len(math_scr_list)))
print("{}% of data for math_scr lies within 2 standard deviations".format(len(math_scr_list_of_data_within_2_std_deviation)*100.0/len(math_scr_list)))
print("{}% of data for math_scr lies within 3 standard deviations".format(len(math_scr_list_of_data_within_3_std_deviation)*100.0/len(math_scr_list)))
print("{}% of data for reading_scr lies within 1 standard deviation".format(len(reading_scr_list_of_data_within_1_std_deviation)*100.0/len(reading_scr_list)))
print("{}% of data for reading_scr lies within 2 standard deviations".format(len(reading_scr_list_of_data_within_2_std_deviation)*100.0/len(reading_scr_list)))
print("{}% of data for reading_scr lies within 3 standard deviations".format(len(reading_scr_list_of_data_within_3_std_deviation)*100.0/len(reading_scr_list)))
print("{}% of data for writing_scr lies within 1 standard deviation".format(len(writing_scr_list_of_data_within_1_std_deviation)*100.0/len(writing_scr_list)))
print("{}% of data for writing_scr lies within 2 standard deviations".format(len(writing_scr_list_of_data_within_2_std_deviation)*100.0/len(writing_scr_list)))
print("{}% of data for writing_scr lies within 3 standard deviations".format(len(writing_scr_list_of_data_within_3_std_deviation)*100.0/len(writing_scr_list)))