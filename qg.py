import pandas as pd 
from pipelines import pipeline
import json
import time

start = time.time()
abstract_df = pd.read_csv('/home/aliciescont/Documents/tfm_code/QA_eval/SimpleDBpediaQA/V1/abstract_df.csv')

nlp_qg = pipeline("e2e-qg", model="valhalla/t5-base-e2e-qg")

abst_list = []

for question in abstract_df['abstract']:
    abst_list.append(nlp_qg(question))

abstract_dict = {}

keys = abstract_df['book']
values = abst_list

abstract_dict = dict(zip(keys, values))


with open("abstract.json", "wb") as f:
    f.write(json.dumps(abstract_dict). encode("utf-8"))