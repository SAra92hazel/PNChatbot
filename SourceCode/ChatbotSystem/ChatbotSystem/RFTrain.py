import sys
import pandas as pd
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
import pickle

class RFTrain:

    def detecting(self,train_file):
        train_news = pd.read_csv(train_file)
        tfidf = TfidfVectorizer(stop_words='english',use_idf=True,smooth_idf=True) #TF-IDF
        print("Start RandomForest Classification")
        knn_pipeline = Pipeline([('lrgTF_IDF', tfidf), ('lrg_RF', RandomForestClassifier(n_estimators=100, max_depth=2))])
        filename = 'rf_model.sav'
        pickle.dump(knn_pipeline.fit(train_news['review'], train_news['sentiment']), open(filename, 'wb'))

        print("RandomForest Model Successfully Trained")


if __name__ == "__main__":
	r=RFTrain()
	r.detecting("dataset.csv")

