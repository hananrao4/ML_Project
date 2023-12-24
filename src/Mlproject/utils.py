import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd 
# from dotenv import load_dotenv
import pyodbc

import pickle
import numpy as np


def read_sql_data():

    logging.info("Reading SQL database started")

    try:
        mydb=pyodbc.connect(
            Driver ='{SQL Server}',               
            Server = 'RAO-HANAN',
            Database = 'Northwind',
            username = 'hananrao1',
            password = 'hananrao825825'
        )
        # logging.info("Connection Established",mydb)
        df=pd.read_sql_query('Select top(1000) * from Student',mydb)
        print(df.head())

        return df
    
    except Exception as ex:
        raise CustomException(ex)
    
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
