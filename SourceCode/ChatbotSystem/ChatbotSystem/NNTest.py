
import sys
import pandas as pd
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
import pickle
from sklearn.neural_network import MLPClassifier

class NNTest:

    def detecting(test_file):
        test_news = pd.read_csv(test_file)
        filename = 'nn_model.sav'
        train = pickle.load(open(filename, 'rb'))
        predicted_class = train.predict(test_news["review"])
        return predicted_class


if __name__ == "__main__":
    r=NN.detecting('testset.csv')


