from typing import Annotated, Union
    # @title Default title text
#import matplotlib.pyplot as plt

import pandas as pd
from io import StringIO
from fastapi import FastAPI, Query
import json
app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[Union[list[str], None], Query()] = None):
    query_items = parse_input(q) 
    
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
def create_dataframe(csv_data):
    # Create a StringIO object to simulate reading from a file-like object
    csv_file = StringIO(csv_data)

    # Read the CSV data into a Pandas DataFrame
    df = pd.read_csv(csv_file, encoding='utf-8')

    # Close the StringIO object
    csv_file.close()

    return df

def data_frame():
    # Define CSV data for each table
    csv_data_Table1 = """المدة البينية,درجة التعين,المؤهل
    5,7,بكالوريوس
    5,8,دبلوم
    5,9,ثانوية صناعية / تجارية
    5,10,ثانوية عامة
    5,11,اعدادية
    5,12,ابتدائية
    5,13,بدون مؤهل"""

    csv_data_Table2 = """المدة البينية,درجة التعين,المؤهل
    4,7,بكالوريوس
    4,8,دبلوم
    4,9,ثانوية صناعية / تجارية
    4,10,ثانوية عامة
    5,11,اعدادية
    5,12,ابتدائية
    5,13,بدون مؤهل"""

    csv_data_Table3 = """درجة التعين,المؤهل
    6,دكتوراه
    7,ماجستير
    7,بكالوريوس
    8,دبلوم فوق المتوسط
    9,ثانوية عامة
    10,اعدادية
    11,ابتدائية
    13,بدون مؤهل"""

    csv_data_3_1 = """المدة البينية,الدرجات ,المؤهل
    ,1,دكتوراه
    4,2,
    4,3,
    3,4,
    3,5,
    2,6,"""

    csv_data_3_2 = """المدة البينية,الدرجات ,المؤهل
    4,1,ماجستير
    4,2,
    4,3,
    3,4,
    3,5,
    3,6,
    2,7,"""

    csv_data_3_4 = """المدة البينية,الدرجات ,المؤهل
    4,1,بكالوريوس
    4,2,
    4,3,
    3,4,
    3,5,
    3,6,
    3,7,"""

    csv_data_3_5 = """المدة البينية,الدرجات ,المؤهل
    4,2,دبلوم فوق المتوسط
    4,3,
    4,4,
    4,5,
    4,6,
    4,7,
    4,8,"""

    # Additional tables
    csv_data_3_6 = """المدة البينية,الدرجات ,المؤهل
    4,3,ثانوية عامة
    4,4,
    4,5,
    4,6,
    4,7,
    4,8,
    4,9,"""

    csv_data_3_7 = """المدة البينية,الدرجات ,المؤهل
    4,4,اعدادية
    4,5,
    4,6,
    4,7,
    4,8,
    4,9,
    4,10,"""

    csv_data_3_8 = """المدة البينية,الدرجات ,المؤهل
    4,5,ابتدائية
    4,6,
    4,7,
    4,8,
    4,9,
    4,10,
    4,11,"""

    csv_data_3_9 = """المدة البينية,الدرجات ,المؤهل
    4,6,بدون مؤهل
    4,7,
    4,8,
    4,9,
    4,10,
    4,11,
    4,12,
    4,13,"""

    # Additional tables
    csv_data_Table4 = """درجة التعين,المؤهل
    6,دكتوراه
    7,ماجستير
    7,بكالوريوس
    8,دبلوم فوق المتوسط
    9,ثانوية عامة
    10,اعدادية
    11,ابتدائية
    13,بدون مؤهل"""

    csv_data_4_1 = """المدة البينية,الدرجات ,المؤهل
    ,-1,دكتوراه
    5,0,
    5,1,
    4,2,
    4,3,
    3,4,
    3,5,
    2,6,"""

    csv_data_4_2 = """المدة البينية,الدرجات ,المؤهل
    ,-1,ماجستير
    5,0,
    5,1,
    4,2,
    4,3,
    3,4,
    3,5,
    3,6,
    2,7,"""

    csv_data_4_3 = """المدة البينية,الدرجات ,المؤهل
    ,-1,بكالوريوس
    5,0,
    5,1,
    4,2,
    4,3,
    3,4,
    3,5,
    3,6,
    3,7,"""

    csv_data_4_4 = """المدة البينية,الدرجات ,المؤهل
    ,0,دبلوم فوق المتوسط
    5,1,
    4,2,
    4,3,
    4,4,
    4,5,
    4,6,
    4,7,
    4,8,"""

    csv_data_4_5 = """المدة البينية,الدرجات ,المؤهل
    ,0,ثانوية عامة
    5,1,
    5,2,
    4,3,
    4,4,
    4,5,
    4,6,
    4,7,
    4,8,
    4,9,"""

    csv_data_4_6 = """المدة البينية,الدرجات ,المؤهل
    ,1,اعدادية
    5,2,
    5,3,
    4,4,
    4,5,
    4,6,
    4,7,
    4,8,
    4,9,
    4,10,"""

    csv_data_4_7 = """المدة البينية,الدرجات ,المؤهل
    ,2,ابتدائية
    5,3,
    5,4,
    4,5,
    4,6,
    4,7,
    4,8,
    4,9,
    4,10,
    4,11,"""

    # Create DataFrames for each table
    df_table_1 = create_dataframe(csv_data_Table1)
    df_table_2 = create_dataframe(csv_data_Table2)
    df_table_3 = create_dataframe(csv_data_Table3)
    df_table_3_1 = create_dataframe(csv_data_3_1)
    df_table_3_2 = create_dataframe(csv_data_3_2)
    df_table_3_4 = create_dataframe(csv_data_3_4)
    df_table_3_5 = create_dataframe(csv_data_3_5)

    # Additional tables
    df_table_3_6 = create_dataframe(csv_data_3_6)
    df_table_3_7 = create_dataframe(csv_data_3_7)
    df_table_3_8 = create_dataframe(csv_data_3_8)
    df_table_3_9 = create_dataframe(csv_data_3_9)

    # Additional tables
    df_table_4 = create_dataframe(csv_data_Table4)
    df_table_4_1 = create_dataframe(csv_data_4_1)
    df_table_4_2 = create_dataframe(csv_data_4_2)
    df_table_4_3 = create_dataframe(csv_data_4_3)
    df_table_4_4 = create_dataframe(csv_data_4_4)
    df_table_4_5 = create_dataframe(csv_data_4_5)
    df_table_4_6 = create_dataframe(csv_data_4_6)
    df_table_4_7 = create_dataframe(csv_data_4_7)

    # Print the resulting DataFrames
    print("Table 1:")
    print(df_table_1)

    print("Table 2:")
    print(df_table_2)

    print("Table 3:")
    print(df_table_3)

    print("Table 3.1:")
    print(df_table_3_1)

    print("Table 3.2:")
    print(df_table_3_2)

    print("Table 3.4:")
    print(df_table_3_4)

    print("Table 3.5:")
    print(df_table_3_5)

    # Additional tables
    print("Table 3.6:")
    print(df_table_3_6)

    print("Table 3.7:")
    print(df_table_3_7)

    print("Table 3.8:")
    print(df_table_3_8)

    print("Table 3.9:")
    print(df_table_3_9)

    # Additional tables
    print("Table 4:")
    print(df_table_4)

    print("Table 4.1:")
    print(df_table_4_1)

    print("Table 4.2:")
    print(df_table_4_2)

    print("Table 4.3:")
    print(df_table_4_3)

    print("Table 4.4:")
    print(df_table_4_4)

    print("Table 4.5:")
    print(df_table_4_5)

    print("Table 4.6:")
    print(df_table_4_6)

    print("Table 4.7:")
    print(df_table_4_7)
