# Question Answering system over DBpedia Knowledge Graph

This project aims to build a QA system for questions of books stored in the DBpedia Knowledge graph, done as the final project of Master od Data Science at UOC.

The QA system is focus on simple questions about books, using as a baseline SimpleDBpediaQA dataset.

### QA tasks

#### Named Entity Linking
Input: question

Output: annotated entity (DBpedia KG) 

Was done by using Tagme https://sobigdata.d4science.org/web/tagme/tagme-help

#### Intent recognition
Input: question

Output: intent

The first version of this QA system was designed to detect the following intents: author of a book, book from author, genre of a book, books in a genre, publisher, publication language, publication date and publisher.

EDA_datasets.ipynb contains a notebook with the process followed for dataset exploration, pre-precessing and LSTM model.

Model using simpletransformer was done in simpletransformer_intent_recognition.ipynb

#### Query construction
Input: intent detected

Output: SPARQL query

qa_main.ipynb contains a summary of all building blocks of this QA system. The first version of this QA system is based on question that maps with only one triple of the DBpedia KG

