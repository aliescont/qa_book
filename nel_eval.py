import pandas as pd 
import numpy as np 
import spotlight
import requests
import time
import json

book_df = pd.read_csv('data_outputs/book_df.csv')

#tagme token
TOKEN = "f70577ab-c371-4fb8-83f3-e82791f9b1a1-843339462"

def NEL_spotlight(question, support):

    question_annotations = []
    try: 
        annotations = spotlight.annotate('https://api.dbpedia-spotlight.org/en/annotate', question, confidence=0.4, support=20) 
        question_annotations.append(annotations[0]['URI']) 
    except:
        question_annotations.append('') 

    return question_annotations[0]


def tagme_annotation(token, question):
    ann_list = []
    response = requests.get("https://tagme.d4science.org/tagme/tag?lang=en&gcube-token={}&text={}".format(token, question))

    annotations = {}
    if response.status_code == 200 :
      for annotation in json.loads(response.text)['annotations']: 
             
        annotations[('http://dbpedia.org/resource/' + annotation['title'].replace(' ', '_'))] = annotation['rho']
    else: 
      annotations.append('')

    return sorted(annotations.items(), key=lambda x: x[1])[-1]



book_df['tagme'] = [tagme_annotation(TOKEN, question)[0] for question in book_df['Query']]
book_df['tagme_rho'] = [tagme_annotation(TOKEN, question)[1] for question in book_df['Query']]


for sup in [0.3, 0.4, 0.5, 0.6]:
    col = 'spot'+str(sup)
    book_df[col] = [NEL_spotlight(question, sup) for question in book_df['Query']]


book_df.to_csv('data_outputs/nel_data.csv', index = False)

print(book_df.head())

def qa_pred (data, pred):
    true = []
    not_ent = []
    for i in range(len(data)):
        if pred[i] == ' ':
            true.append(0.0)
            not_ent.append(1.0)
        elif pred[i] == data[i]:
            true.append(1.0)
        else:
            true.append(0.0)

    fp = len(data)-sum(not_ent)-sum(true)
    fn = len(data)-sum(true)
    recall = sum(true)/(sum(true)+fn)
    precision = sum(true)/(sum(true)+fp)
    return recall, precision, sum(true), fp, fn
