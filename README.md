# Question Answering system over DBpedia Knowledge Graph

This project aims to build a QA system for questions of books stored in the DBpedia Knowledge graph, done as the final project of Master of Data Science at UOC.

The QA system is focus on simple questions about books, using as a baseline SimpleDBpediaQA dataset.

The QA system pipeline consists of five main blocks that combines off-the-shelf components, classification algorithms and rule-based approach

### QA system blocks

#### Named Entity Linking
This block translate the question in natural language into a concept in the DBpedia Knowledge Graph. It was done by using off-the-shelf QA components, such as DBpedia Spotlight and TagMe

Input: question in natural lamguage

Output: annotated entity (DBpedia KG) 

Tagme https://sobigdata.d4science.org/web/tagme/tagme-help

#### Intent recognition
This task was done by using a multiclass classification algorithm , evaluating the performance of LSTM over BERT

Dataset: SimpleDBpediaQA filtered and processed to adapt to book domain questions.

Input: question in natural language

Output: intent

The first version of this QA system was designed to detect the following intents: author of a book, book from author, genre of a book, books in a genre, publisher, publication language, publication date and publisher.

EDA_datasets.ipynb contains a notebook with the process followed for dataset exploration, pre-precessing and LSTM model.

Model using simpletransformer was done in simpletransformer_intent_recognition.ipynb

#### Query construction and answer block
This block was built using a rule-based approach, defining templates of SPARQL queries based on the intent detected in the previous block

Input: intent detected

Output: SPARQL query

qa_main.ipynb contains a summary of all building blocks of this QA system. The first version of this QA system is based on question that maps with only one triple of the DBpedia KG

