import pandas as pd
import gc
import os
import numpy as np
import time
import dask.dataframe as dd
import csv

# key_to_search = input('Enter the searching element: ')
key_to_search = 'CORN'
start = time.time()
dtypes = {

    "RKY": "object",
    "LOCAT": "str",
    "ACTION": "str",
    "TRUCK": "str",
    "BUS": "str",
    "FID": "uint8"

}

# data = dd.read_csv('traffic_crashes.csv', delimiter=",")
data = pd.read_csv('traffic_crashes.csv', delimiter=",")
# data = csv.reader(open('traffic_crashes.csv', "r"), delimiter=",")
# pd_df = data.compute()
# ddf_select= dd[]

# print(data)
# print(data.partitions)
# print("Train size:", pd_df.shape)
for row in data:
    # print(row)
    if key_to_search == row[1]:
        print(row)

end = time.time()
print(end - start, 'sec')
