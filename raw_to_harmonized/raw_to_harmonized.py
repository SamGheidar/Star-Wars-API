from operator import index
import requests
import pandas as pd
import os
import json

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
json_data_path = os.path.abspath(os.path.join(CURR_DIR_PATH, os.pardir))
json_data_path += "/data/testing/raw/data.json"

def json_to_tuples(x):
    f = open(x)
    data = json.load(f)
    f.close()
    new_data = tuple(data)
    
    for key in new_data:
        print(key)
    #print(type(new_data))
    #return key



json_to_tuples(json_data_path)



