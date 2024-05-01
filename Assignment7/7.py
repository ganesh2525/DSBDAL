# 1-dowload necesary things from nltk
# 2-tokenization
# 3-pos tagging
# 4-stop words removal
# 5-stemming
# 6-lemmatization
# 7-TF-IDF

# pip install nltk

import nltk
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("averaged_perceptron_tagger")


from nltk import word_tokenize, sent_tokenize 
corpus = "Sachin was the GOAT of the previous generation. Virat is the GOAT of this generation. No one will be the GOAT of next geneartion." 
print(word_tokenize(corpus))
print(sent_tokenize(corpus))


from nltk import pos_tag
tokens = word_tokenize(corpus)
print(pos_tag(tokens))


from nltk.corpus import stopwords
tokens = word_tokenize(corpus)
stop_words = set(stopwords.words("english"))
cleaned_tokens = []
for token in tokens:
    if (token not in stop_words):
        cleaned_tokens.append(token)
print(cleaned_tokens)


from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
stemmed_tokens = []
for token in cleaned_tokens:
    stemmed = stemmer.stem(token)
    stemmed_tokens.append(stemmed)
print(stemmed_tokens)


from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = []
for token in cleaned_tokens:
    lemmatized = lemmatizer.lemmatize(token)
    lemmatized_tokens.append(lemmatized)
print(lemmatized_tokens)


from sklearn.feature_extraction.text import TfidfVectorizer
corpus = [
    "Sachin was the GOAT of previous generation",
    "Virat is the GOAT of this generation",
    "Shubham will be the GOAT of next generation"
]
vectorizer = TfidfVectorizer()

print(vectorizer.fit(corpus).vocabulary_)
print(vectorizer.transform(corpus))
print(vectorizer.get_feature_names_out())


import math

def TF(doc,term):
    words = doc.split()  # Split document into words
    term_count = words.count(term)  # Count occurrences of the term
    total_terms = len(words)  # Total number of terms in the document
    tf = term_count / total_terms  # Calculate TF
    return tf

def IDF(docs, term):
    doc_count = sum(1 for doc in docs if term in doc)  # Count documents containing the term
    total_docs = len(docs)  # Total number of documents
    idf = math.log(total_docs / (1 + doc_count))  # Calculate IDF
    return idf

documents = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?",
]

term = "This"
tf = TF(documents[0], term)
idf = IDF(documents, term)

print("TF:", tf)
print("IDF:", idf)
print("TF-IDF:",tf*idf) 