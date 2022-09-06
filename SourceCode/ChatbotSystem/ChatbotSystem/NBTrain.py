import sys
import pandas as pd
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
import pickle

class NBTrain:

    def detecting(self,train_file):
        train_news = pd.read_csv(train_file)
        tfidf = TfidfVectorizer(stop_words='english',use_idf=True,smooth_idf=True) #TF-IDF
        print("Start NB Classification")
        nb_pipeline = Pipeline([('lrgTF_IDF', tfidf), ('lrg_nb', MultinomialNB())])
        filename = 'nb_model.sav'
        pickle.dump(nb_pipeline.fit(train_news['review'], train_news['sentiment']), open(filename, 'wb'))
        print("NB Model Successfully Trained")

if __name__ == "__main__":
    nb=NBTrain()
    nb.detecting("dataset.csv")