from operator import index
import requests
import pandas as pd
import os
import json
url_1 = "https://swapi.dev/api"
url_2 = "https://swapi.dev/api/people"
CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
testing = CURR_DIR_PATH + "data/testing/raw/"

response = requests.get(url_1)

#Write a function that does a request to a URL and returns the resource as a Python dict.
def python_dict(url):
    response = requests.get(url)
    return response.json()



#In the same file, write another function that takes a Python dict and a filepath and saves the dict as a JSON object in that path.
def save_json(dictionary):
    df = pd.DataFrame(dictionary)
    df.to_json("data/testing/raw/data.json", orient="records")
    df.to_csv("data/testing/raw/data.csv")
    df.to_html("data/testing/raw/data.html")

response = python_dict("https://swapi.dev/api/people")
save_json(response)


# f = open("source_to_raw/data.json", "w")
# f.write(data.json)
# f.close()



