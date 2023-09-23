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
        df = pd.read_csv(file_path)
        
        # Extract the filename (without extension) as the key for the dictionary
        key = os.path.splitext(file_name)[0]
        
        # Store the DataFrame in the dictionary
        dataframes[key] = df

    return dataframes

data_folder_path = "./data"  # Replace with your actual path
dataframes = create_dataframes_from_csv(data_folder_path)

print("Keys:", dataframes.keys())
for key, df in dataframes.items():
    print("\nDataFrame for key:", key)
    print(df)


query_items :dict = {} 
query_items_test :dict = {'numCertificates': 1, 'disContinuousPeriods': 0, 'Academic Certificate Name 1': 0, 'Date of Acquiring 1': '2023-09-14T21:00:00.000Z', 'Academic Certificate Name 2': 4, 'Date of Acquiring 2': '2023-09-08T21:00:00.000Z', 'Academic Certificate Name 3': 1, 'Date of Acquiring 3': '2023-09-01T21:00:00.000Z', 'Date of Employment': '1970-09-02T21:00:00.000Z', 'Your Current Performance Evaluation': 'ممتاز', 'Result of the Custom Calculator': 'Calculate', 'Range 1 Years': 0, 'Range 2 Years': 0, 'Range 3 Years': 0, 'Range 4 Years': 0}
dataframes_list = []
   


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


# To do :
def map_qualification_to_numerical(df, qualification_column):
    """
    Map the qualification column in the DataFrame to numerical values based on the CertificateOptions enum.

    Parameters:
    df (pandas.DataFrame): DataFrame containing the qualification column.
    qualification_column (str): Name of the qualification column to be mapped.

    Returns:
    pandas.DataFrame: DataFrame with an additional column for the numerical representation of the qualification.
    """
    def map_qualification(qualification):
        try:
            return CertificateOptions[qualification].value
        except KeyError:
            return None  # or handle accordingly if the qualification is not found

    # Apply the function to the specified qualification column and create a new column for the numerical representation
    df['Numerical_Qualification'] = df[qualification_column].apply(map_qualification)

    return df



for df in dataframes_list:
   # df = map_qualification_to_numerical(df, 'المؤهل')
    print(df)
    print('------------------------')
#print(CertificateOptions.دكتوراة.value)


app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[Union[list[str], None], Query()] = None):
    global query_items

    query_items = parse_input(q) 
  #  print(query_items)
    
    
    return query_items


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



    dateOfEmployment = datetime.datetime.strptime(date_of_employment, '%Y-%m-%dT%H:%M:%S.%fZ')
    range_name = ''
    range_number = 0

    range1_start = datetime.datetime.strptime('1/1/1967', '%m/%d/%Y').strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    range1_end = datetime.datetime.strptime('9/9/2002', '%m/%d/%Y').strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    range2_start = datetime.datetime.strptime('10/9/2002', '%m/%d/%Y').strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    range2_end = datetime.datetime.strptime('1/4/2009', '%m/%d/%Y').strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    range3_start = datetime.datetime.strptime('2/4/2009', '%m/%d/%Y').strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    range3_end = datetime.datetime.strptime('1/1/2016', '%m/%d/%Y').strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    range4_start = datetime.datetime.strptime('2/1/2016', '%m/%d/%Y').strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    current_date = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')

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


#
#Case#1 assuming no discontinous periods : 
def case_1():

    print(query_items_test['Date of Employment'])
    print(date_renges(query_items_test['Date of Employment'])[1])  # get the date of employment to know from which range to start , assuming no discontinous periods .
    print(query_items_test['Academic Certificate Name 1']) # get the first certificate name to know from which rank to start 
    range_to_start = date_renges(query_items_test['Date of Employment'])[1]
    if range_to_start == 1:
        pass    
    elif range_to_start == 2:
        pass    
    elif range_to_start == 3:
        pass
    elif range_to_start == 4:
        pass
    rank_to_start = query_items_test['Academic Certificate Name 1']




#Testing block 
#print(date_renges('2018-09-02T21:00:00.000Z'))

#case_1()

#end Testing block 