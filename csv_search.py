import pandas as pd
import gc
import os
import numpy as np
import time
import dask.dataframe as dd
import csv
# key_to_search = input('Enter the searching element: ')

#optimised one
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
# data = pd.read_csv('traffic_crashes.csv', delimiter=",")
data = dd.read_csv('traffic_crashes.csv', delimiter=",")
# data = csv.reader(open('traffic_crashes.csv', "r"), delimiter=",")

end = time.time()
print(end - start, 'sec')

print(data[data['LOCAT'] == 'CORN'].head())

