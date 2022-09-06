import sys
import pandas as pd
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
import pickle
from sklearn.neural_network import MLPClassifier

class NNTrain:

    def detecting(self,train_file):
        train_news = pd.read_csv(train_file)
        tfidf = TfidfVectorizer(stop_words='english',use_idf=True,smooth_idf=True) #TF-IDF
        print("Start NN Classification")
        svm_pipeline = Pipeline([('lrgTF_IDF', tfidf), ('lrg_mn', MLPClassifier())])
        
        filename = 'nn_model.sav'
        pickle.dump(svm_pipeline.fit(train_news['review'], train_news['sentiment']), open(filename, 'wb'))

        print("NN Model Successfully Trained")


if __name__ == "__main__":
	r=NNTrain()
	r.detecting("dataset.csv")

