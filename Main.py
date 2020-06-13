# test
# print("Hello welcome to the data analysis")

# panda try
# import pandas as pd
#
# dataFromCSV = pd.read_csv("/home/poojan/Downloads/Quiz_Performance_By_User_vishal.shukla@brevitaz.com_20191225_020125_file1.csv")
# print(dataFromCSV.describe())
# print(dataFromCSV.dtypes)
# print(dataFromCSV.info())

# csv to es
#
# import csv
# import json
# from elasticsearch import Elasticsearch
#
# def insert_es(fname):
#     es = Elasticsearch([{'host':'localhost','port':'9200'}])
#     i = 1
#     reader = csv.DictReader(fname)
#     for row in reader:
#         es.index(index="test", doc_type="practice", id=i, body=json.dumps(row))
#         i=i+1
#
#
# with open("/home/poojan/Downloads/Quiz_Performance_By_User_vishal.shukla@brevitaz.com_20191225_020125_file1.csv") as fname:
#     insert_es(fname)