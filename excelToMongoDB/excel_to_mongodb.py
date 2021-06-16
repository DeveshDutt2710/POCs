
# run command in terminal like below
# python excel_to_mongodb.py ChangeDepartmentalElectives.xlsx

import sys
import os
import pandas as pd
from pymongo import MongoClient  


filename = sys.argv[1]
read_file = pd.read_excel(filename)

read_file.to_csv("Test.csv", index = None,header=True)


os.system("mongoimport --host=127.0.0.1:27017 -d excel_to_mongodb -c excel_mongodb --type csv --file Test.csv --headerline")


os.remove('Test.csv')