#-------------------------------------------------------------------------
# AUTHOR: Brandon Diep
# FILENAME: indexing.py
# SPECIFICATION: This program will read the file colllection.csv and output the tf-idf document-term matrix
# FOR: CS 5180- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#Importing some Python libraries
import csv
import math

documents = []

#Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append(row[0])

#Conducting stopword removal for pronouns/conjunctions. Hint: use a set to define your stopwords.
#--> add your Python code here
stopWords = {'I', 'and', 'She', 'her', 'They', 'their'}

for i in range(len(documents)):
    for stop in stopWords:
        documents[i] = documents[i].replace(stop,"").strip()

#Conducting stemming. Hint: use a dictionary to map word variations to their stem.
#--> add your Python code here
stemming = {"cats": "cat", "dogs": "dog", "loves": "love"}

for i in range(len(documents)):
    for stem in stemming.keys():
        documents[i] = documents[i].replace(stem,stemming[stem])


#Identifying the index terms.
#--> add your Python code here
indexTerms = []
indexTermList = []
for doc in documents:
    doc = doc.split()
    indexTermList.append(doc)
    for term in doc:
        if term not in indexTerms:
            indexTerms.append(term)

print(indexTermList)


#Building the document-term matrix by using the tf-idf weights.
#--> add your Python code here

docTermMatrix = []

# remove duplicate words from the index terms
indexTermSet = list(map(set, indexTermList))
# new list without duplicates
docTermList = list(map(list, indexTermSet))

# go through each document in indexTermList and its terms for that doc
for i, doc in enumerate(indexTermList):
    TF = []
    IDF = []
    TF_IDF = []
    # given all the possible terms, calculate the tf-idf for each document term
    for term in indexTerms:
        TF = doc.count(term) / len(indexTermList[i])

        DF = 0
        # loop through the doc index terms and count for current term, [['cat', 'love'], ['love', 'dog'], ['cat', 'love', 'dog']]
        for indexTerm in docTermList:
            DF += indexTerm.count(term)

        IDF = math.log(len(indexTermList) / DF, 10)
        TF_IDF.append(TF * IDF)
    docTermMatrix.append(TF_IDF)


#Printing the document-term matrix.
#--> add your Python code here
print(docTermMatrix)