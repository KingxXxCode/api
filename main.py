# -*- coding: utf-8 -*-
from typing import Annotated, Union
import datetime
    # @title Default title text
#import matplotlib.pyplot as plt

import pandas as pd
from io import StringIO
from fastapi import FastAPI, Query
import json

from enum import Enum, auto
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
import math
from dateutil.relativedelta import relativedelta
def calculate_rank_and_remainder_case_1(years, rank, years_to_promote):
    """
    Calculate the updated rank and the remaining years after promotions.

    Parameters:
    years (int): Total years spent.
    rank (int): Current rank.
    years_to_promote (int): Number of years to promote for each rank increase.

    Returns:
    list: [updated_rank, remaining_years]
    """
    while years >= years_to_promote:
        years -= years_to_promote
        rank -= 1
    return [rank, max(0, years)]
def calculate_intersection_table3( period2_start_str, period2_end_str):
    range_name = 'Range 3: 2/4/2009 - 1/1/2016'
    range_number = 3
    #Table 4 range_name = 'Range 4: 2/1/2016 - ' + current_date
    # Extract start and end dates for period #1
    parts = range_name.split(' ')
    if len(parts) < 3:
        raise ValueError("Invalid format for period1")

    # Extract and parse start and end dates for period #1
    period1_start = datetime.strptime(parts[-3], '%d/%m/%Y')
    period1_end = datetime.strptime(parts[-1], '%d/%m/%Y')

    # Convert period2 start and end strings to datetime objects
    period2_start = datetime.strptime(period2_start_str, '%Y-%m-%dT%H:%M:%S.%fZ')
    period2_end = datetime.strptime(period2_end_str, '%Y-%m-%dT%H:%M:%S.%fZ')

    # Find the intersection between the periods
    intersection_start = max(period1_start, period2_start)
    intersection_end = min(period1_end, period2_end)

    # Calculate the difference in years and remaining months for the intersection
    difference = relativedelta(intersection_end, intersection_start)
    years_difference = difference.years
    months_difference = difference.months

    return [years_difference, months_difference]

def calculate_intersection_table4( period2_start_str, period2_end_str):
   # range_name = 'Range 3: 2/4/2009 - 1/1/2016'
    range_number = 4
    range_name = 'Range 4: 2/1/2016 - ' + get_current_time()
    # Extract start and end dates for period #1
    parts = range_name.split(' ')
    if len(parts) < 3:
        raise ValueError("Invalid format for period1")

    # Extract and parse start and end dates for period #1
    period1_start = datetime.strptime(parts[-3], '%d/%m/%Y')
    period1_end = datetime.strptime(parts[-1], '%d/%m/%Y')

    # Convert period2 start and end strings to datetime objects
    period2_start = datetime.strptime(period2_start_str, '%Y-%m-%dT%H:%M:%S.%fZ')
    period2_end = datetime.strptime(period2_end_str, '%Y-%m-%dT%H:%M:%S.%fZ')

    # Find the intersection between the periods
    intersection_start = max(period1_start, period2_start)
    intersection_end = min(period1_end, period2_end)

    # Calculate the difference in years and remaining months for the intersection
    difference = relativedelta(intersection_end, intersection_start)
    years_difference = difference.years
    months_difference = difference.months

    return [years_difference, months_difference]


def calculate_intersection(period1_str, period2_start_str, period2_end_str):
    # Extract start and end dates for period #1
    parts = period1_str.split(' ')
    if len(parts) < 3:
        raise ValueError("Invalid format for period1")

    # Extract and parse start and end dates for period #1
    period1_start = datetime.strptime(parts[-3], '%d/%m/%Y')
    period1_end = datetime.strptime(parts[-1], '%d/%m/%Y')

    # Convert period2 start and end strings to datetime objects
    period2_start = datetime.strptime(period2_start_str, '%Y-%m-%dT%H:%M:%S.%fZ')
    period2_end = datetime.strptime(period2_end_str, '%Y-%m-%dT%H:%M:%S.%fZ')

    # Find the intersection between the periods
    intersection_start = max(period1_start, period2_start)
    intersection_end = min(period1_end, period2_end)

    # Calculate the difference in years and remaining months for the intersection
    difference = relativedelta(intersection_end, intersection_start)
    years_difference = difference.years
    months_difference = difference.months

    return [years_difference, months_difference]

def calculate_rank_and_remainder_case_2(years, rank,Certificate_name):
    print("Years"+str(years))
    print("rank "+str(rank))
    list_of_years_to_promote = []
    list_of_Ranks=[]
#1- know which table to use 
    tablename=(SubTableOptions.get_text(Certificate_name))
#2- start leveling up ..
    for key, df in dataframes.items():
        if key == tablename:
            for i in range(len(df)-1, -1, -1):
                # Do something with the current row
                if  math.isnan((df.iloc[i].values[0])):
                   pass
                   #  print("got nan")
                else:
                    list_of_years_to_promote.append(int(df.iloc[i].values[0]))
                if  math.isnan((df.iloc[i].values[1])):
                     pass
                     #print("got nan")
                else:
                    list_of_Ranks.append(int(df.iloc[i].values[1]))
            #print(list_of_years_to_promote)
           # print(list_of_Ranks)
#3- before this i need to know if i have started at rank 6 or higher from prev tables
    index_to_start=(list_of_Ranks.index(rank))
    for a in range(len(list_of_years_to_promote)):
            
            if a>=(index_to_start):
                if (years - list_of_years_to_promote[a])>0:
                
                 
       
                 years -= list_of_years_to_promote[a]
                 rank -= 1
                else:
                     break
    #print("----")
   # print(years,rank)



    return {"years_reminder":years , "rank": rank}
def get_current_time():
    current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    return current_time

def create_dataframes_from_csv(folder_path):
    # Get a list of all files in the data folder
    file_names = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

    # Initialize an empty dictionary to store DataFrames
    dataframes = {}

    # Iterate through each file and create a DataFrame
    for file_name in file_names:
        # Construct the full path to the CSV file
        file_path = os.path.join(folder_path, file_name)
        
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path,index_col=None)
        
        # Extract the filename (without extension) as the key for the dictionary
        key = os.path.splitext(file_name)[0]
        
        # Store the DataFrame in the dictionary
        dataframes[key] = df

    return dataframes

data_folder_path = "./data"  # Replace with your actual path
dataframes = create_dataframes_from_csv(data_folder_path)

#print("Keys:", dataframes.keys())
#for key, df in dataframes.items():
#    print("\nDataFrame for key:", key)
#    print(df)


query_items :dict = {} 
query_items_test :dict = {'numCertificates': 1, 'disContinuousPeriods': 0, 'Academic Certificate Name 1': 0, 'Date of Acquiring 1': '2023-09-14T21:00:00.000Z', 'Academic Certificate Name 2': 4, 'Date of Acquiring 2': '2023-09-08T21:00:00.000Z', 'Academic Certificate Name 3': 1, 'Date of Acquiring 3': '2023-09-01T21:00:00.000Z', 'Date of Employment': '1970-09-02T21:00:00.000Z', 'Your Current Performance Evaluation': 'ممتاز', 'Result of the Custom Calculator': 'Calculate', 'Range 1 Years': 0, 'Range 2 Years': 0, 'Range 3 Years': 0, 'Range 4 Years': 0}
query_items_test_case2 :dict =  {"numCertificates":1,"disContinuousPeriods":2,"Academic Certificate Name 1":5,"Date of Acquiring 1":"2007-12-31T21:00:00.000Z","Date of Employment #1 start":"2009-12-31T21:00:00.000Z","Date of Employment #1 end":"2012-12-31T21:00:00.000Z","Date of Employment #2 start":"2013-12-31T21:00:00.000Z","Date of Employment #2 end":"2015-01-01T21:00:00.000Z","Your Current Performance Evaluation":"","Result of the Custom Calculator":"Calculate","Range 1 Years":0,"Range 2 Years":1.5003422313483916,"Range 3 Years":4,"Range 4 Years":0}
#2#{"numCertificates":1,"disContinuousPeriods":2,"Academic Certificate Name 1":5,"Date of Acquiring 1":"2007-12-31T21:00:00.000Z","Date of Employment #1 start":"2009-12-31T21:00:00.000Z","Date of Employment #1 end":"2012-12-31T21:00:00.000Z","Date of Employment #2 start":"2013-12-31T21:00:00.000Z","Date of Employment #2 end":"2014-12-31T21:00:00.000Z","Your Current Performance Evaluation":"","Result of the Custom Calculator":"Calculate","Range 1 Years":0,"Range 2 Years":1.5003422313483916,"Range 3 Years":4,"Range 4 Years":0}
#1#{"numCertificates":1,"disContinuousPeriods":2,"Academic Certificate Name 1":2,"Date of Acquiring 1":"2007-12-31T21:00:00.000Z","Date of Employment #1 start":"2009-12-31T21:00:00.000Z","Date of Employment #1 end":"2012-12-31T21:00:00.000Z","Date of Employment #2 start":"2013-12-31T21:00:00.000Z","Date of Employment #2 end":"2014-12-31T21:00:00.000Z","Your Current Performance Evaluation":"","Result of the Custom Calculator":"Calculate","Range 1 Years":0,"Range 2 Years":1.5003422313483916,"Range 3 Years":4,"Range 4 Years":0}
#{"numCertificates":1,"disContinuousPeriods":3,"Academic Certificate Name 1":0,"Date of Acquiring 1":"2023-10-04T21:00:00.000Z","Academic Certificate Name 2":1,"Date of Acquiring 2":"2023-10-16T21:00:00.000Z","Date of Employment #1 start":"2009-10-19T21:00:00.000Z","Date of Employment #1 end":"2013-10-29T21:00:00.000Z","Date of Employment #2 start":"2013-10-27T21:00:00.000Z","Date of Employment #2 end":"2016-10-14T21:00:00.000Z","Date of Employment #3 start":"2017-10-26T21:00:00.000Z","Date of Employment #3 end":"2023-10-07T21:00:00.000Z","Your Current Performance Evaluation":"ممتاز","Result of the Custom Calculator":"Calculate","Range 1 Years":1.8015058179329226,"Range 2 Years":5.10609171800137,"Range 3 Years":0.7775496235455168,"Range 4 Years":2.945927446954141}


dataframes_list = []
   


class SubTableOptions(Enum):
    دكتوراة = 'Data-Project-Law - 3.1'
    ماجستير = 'Data-Project-Law - 3.2'
    بكالوريوس = 'Data-Project-Law - 3.4'
    دبلوم = 'Data-Project-Law - 3.5'
    ثانوية_عامة = 'Data-Project-Law - 3.6'
    اعدادية = 'Data-Project-Law - 3.7'
    ابتدائية = 'Data-Project-Law - 3.8'
    بدون_مؤهل = 'Data-Project-Law - 3.9'
    
    @classmethod
    def get_text(cls, value):
        for item in cls:
            #print(item.value)
            if item.name == value:
                return item.value
        raise ValueError(f"No such value in the enum: {value}")



class CertificateOptions(Enum):
    دكتوراة = 0
    ماجستير = 1
    بكالوريوس = 2
    دبلوم = 3
    ثانوية_صناعية_تجارية = 4
    ثانوية_عامة = 5
    اعدادية = 6
    ابتدائية = 7
    بدون_مؤهل = 8
    
    @classmethod
    def get_text(cls, value):
        for item in cls:
            if item.value == value:
                return item.name
        raise ValueError(f"No such value in the enum: {value}")


# To do :

'''

for key, df in dataframes.items():
    # Map qualification to numerical values for the 'المؤهل' column
   
    
    print("\nDataFrame for key:", key)
    print(df)
    print('------------------------')
#print(CertificateOptions.دكتوراة.value)
'''

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[Union[list[str], None], Query()] = None):
    global query_items
    global query_items_test_case2

    query_items = parse_input(q) 
  #  print(query_items)
 #   print("Keys:", dataframes.keys())
 #   for key, df in dataframes.items():
  #      print("\nDataFrame for key:", key)
   #     print(df)
    
   # return query_items
    query_items_test_case2 :dict =query_items
    
    
    
    return query_items
    #case_2()


def parse_input(input_data):
    try:
        # Convert the input JSON-like string into a Python dictionary
        data = json.loads(input_data[0])
        # Convert the values in the first two keys to integers
        for key in data.keys():
            if key in ["numCertificates", "disContinuousPeriods"]:
                try:
                    data[key] = int(float(data[key]))
                except ValueError:
                    # Handle the case where the conversion is not possible
                    pass
                
        # Extract and return the dictionary
        return data
    except Exception as e:
        # Handle any exceptions that may occur during parsing
        return {"error": str(e)}


def date_renges(date_of_employment:str):
    # Check if the 'Date of Employment' falls within any of the specified date ranges



    dateOfEmployment = datetime.strptime(date_of_employment, '%Y-%m-%dT%H:%M:%S.%fZ')
    range_name = ''
    range_number = 0

    range1_start = datetime.strptime('1/1/1967', '%m/%d/%Y').strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    range1_end = datetime.strptime('9/9/2002', '%m/%d/%Y').strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    range2_start = datetime.strptime('10/9/2002', '%m/%d/%Y').strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    range2_end = datetime.strptime('1/4/2009', '%m/%d/%Y').strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    range3_start = datetime.strptime('2/4/2009', '%m/%d/%Y').strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    range3_end = datetime.strptime('1/1/2016', '%m/%d/%Y').strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    range4_start = datetime.strptime('2/1/2016', '%m/%d/%Y').strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    current_date = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')

    if range1_start <= date_of_employment <= range1_end:
        range_name = 'Range 1: 1/1/1967 - 9/9/2002'
        range_number = 1
    elif range2_start <= date_of_employment <= range2_end:
        range_name = 'Range 2: 10/9/2002 - 1/4/2009'
        range_number = 2
    elif range3_start <= date_of_employment <= range3_end:
        range_name = 'Range 3: 2/4/2009 - 1/1/2016'
        range_number = 3
    elif range4_start <= date_of_employment <= current_date:
        range_name = 'Range 4: 2/1/2016 - ' + current_date
        range_number = 4
    return range_name,range_number

#case#2 assuming discontinous periods :
def case_2_Table3(discontinuous_periods: int) -> dict:
    dict_of_years_and_months = {"years": 0, "months": 0}
    #1-findout how many years and months are in this table ? 
    #1.1-get the date of employment for each period
    for a in range(query_items_test_case2['disContinuousPeriods']):
        #print(query_items_test_case2['Date of Employment #'+str(a+1)+' start'])
        #print(query_items_test_case2['Date of Employment #'+str(a+1)+' end'])
        #print(calculate_intersection_table3(query_items_test_case2['Date of Employment #'+str(a+1)+' start'],query_items_test_case2['Date of Employment #'+str(a+1)+' end']))
       # print('------------------------')
        temp = calculate_intersection_table3(query_items_test_case2['Date of Employment #'+str(a+1)+' start'],query_items_test_case2['Date of Employment #'+str(a+1)+' end'])

        if temp[0]>=0:
                dict_of_years_and_months["years"] += temp[0]
        if temp[1]>=0:
                dict_of_years_and_months["months"] += temp[1] 
       # print(dict_of_years_and_months)
       # print('------------------------')

    if dict_of_years_and_months["months"] > 12:
        dict_of_years_and_months["years"] += dict_of_years_and_months["months"] // 12
        dict_of_years_and_months["months"] = dict_of_years_and_months["months"] % 12
   # print(dict_of_years_and_months)

    

    return dict_of_years_and_months    
def case_2()-> int:
    rank=99

#1- get the number of discontinous periods

    time_in_table3=case_2_Table3(query_items_test_case2['disContinuousPeriods'])
    print(time_in_table3)
#2-get the Academic certificate to know which rank to start with . 
    academic_certificate_name=CertificateOptions.get_text(query_items_test_case2['Academic Certificate Name 1'])
    print(academic_certificate_name)
    print('------------------------')
#3- access the Main Table 3 and get the rank for this certificate . 

    for key, df in dataframes.items():
        if key == 'Data-Project-Law - Table3-Mod':
            is_present = df['المؤهل'] == academic_certificate_name
            if is_present.any():
                selected_row = df.loc[is_present, :]
                rank=((selected_row.iloc[0].values[0]))
   # print(rank)
#now i know the rank to start with , and the time spent in table 3 , i can calculate the rank and the remaining years and months
    table_3_list= calculate_rank_and_remainder_case_2(time_in_table3["years"], rank,academic_certificate_name)
    print(table_3_list)
    return table_3_list


#
#Case#1 assuming no discontinous periods : 
def case_1()-> int:

    print(query_items_test['Date of Employment'])  #-->1970-09-02T21:00:00.000Z
    print(date_renges(query_items_test['Date of Employment']))  # get the date of employment to know from which range to start , assuming no discontinous periods . --->('Range 1: 1/1/1967 - 9/9/2002', 1)
    print(query_items_test['Academic Certificate Name 1']) # get the first certificate name to know from which rank to start --->0
    print(CertificateOptions.get_text(query_items_test['Academic Certificate Name 1'])) # get the first certificate name to know from which rank to start--->دكتوراة
    academic_certificate_name=CertificateOptions.get_text(query_items_test['Academic Certificate Name 1'])
    range_to_start = date_renges(query_items_test['Date of Employment'])[1]
    current_time = get_current_time()
    print(current_time)

    for a in range(4):

            if range_to_start == 1:
                for key, df in dataframes.items():
                    if key=='Data-Project-Law - Table1-Mod':
                        print("\nDataFrame for key:", key)
                        is_present = df['المؤهل'].isin([academic_certificate_name])
                        print('Is academic_certificate_name present in the Name column?', is_present.any())
                        if is_present.any()==False:
                                holder=(df.iloc[0])
                                # get how many years and months of experience the employee has with in this table  :
                                try:   
                                    # print((date_renges(query_items_test['Date of Employment'])[0], query_items_test['Date of Employment'], current_time))
                                        intersection_result = calculate_intersection(date_renges(query_items_test['Date of Employment'])[0], query_items_test['Date of Employment'], current_time)
                                        print("Intersection:", intersection_result[0], "years,", intersection_result[1], "months")
                                except ValueError as e:
                                        print("Error:", str(e))
                                #print(holder[1])
                                table_1_list= calculate_rank_and_remainder_case_1(intersection_result[0], holder[1], holder[0])
                                print(table_1_list)
                                range_to_start=2

                                
                    # print(df)
                    # print('------------------------')
                    # print(df.loc[df['المؤهل'] == CertificateOptions.get_text(query_items_test['Academic Certificate Name 1'])])
                    
            # which_rank=dataframes    
            elif range_to_start == 2:
                for key, df in dataframes.items():
                    print('-------------------TAble2-----------------')
                    if key=='Data-Project-Law - table2-Mod':
                        print("\nDataFrame for key:", key)
                        is_present = df['المؤهل'].isin([academic_certificate_name])
                        print('Is academic_certificate_name present in the Name column?', is_present.any())
                        if is_present.any()==False:#To Do : what if True , needs implementation 
                                holder=(df.iloc[0])
                                # get how many years and months of experience the employee has with in this table  :
                                try:   
                                    # print((date_renges(query_items_test['Date of Employment'])[0], query_items_test['Date of Employment'], current_time))
                                        intersection_result = calculate_intersection(date_renges(query_items_test['Date of Employment'])[0], query_items_test['Date of Employment'], current_time)
                                        print("Intersection:", intersection_result[0], "years,", intersection_result[1], "months")
                                except ValueError as e:
                                        print("Error:", str(e))
                                #print(holder[1])
                                table_1_list= calculate_rank_and_remainder_case_1(intersection_result[0], holder[1], holder[0])
                                print(table_1_list)    
            elif range_to_start == 3:
                pass
            elif range_to_start == 4:
                pass
            rank_to_start = query_items_test['Academic Certificate Name 1']




#Testing block 
#print(date_renges('2010-09-02T21:00:00.000Z'))
#print('------------------------')
#print(date_renges(query_items_test['Date of Employment'])[0])
#print('------------------------')




#case_2()

#end Testing block 