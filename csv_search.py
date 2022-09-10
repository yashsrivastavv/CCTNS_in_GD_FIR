import pandas as pd
import numpy as np
import time
import dask.dataframe as dd
import main
# key_to_search = main.work()
key_to_search = main.query

start = time.time()
dtypes = {

    "RKY": "object",
    "LOCAT": "str",
    "ACTION": "str",
    "TRUCK": "str",
    "BUS": "str",
    "FID": "uint8"

}
data = dd.read_csv('traffic_crashes.csv', delimiter=",")
end = time.time()
print(end - start, 'sec')
var = key_to_search.lower()
print(data[data['LOCAT'] == var].head())
print(key_to_search)

