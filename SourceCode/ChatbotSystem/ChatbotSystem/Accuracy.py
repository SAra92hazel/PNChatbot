from RFTest import RFTest
from SVMTest import SVMTest
from NBTest import NBTest
from NNTest import NNTest
import pandas as pd
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
from DBConnection import DBConnection


def model_assessment(y_test, predicted_class):
	accuracy = accuracy_score(y_test, predicted_class)
	return accuracy


def ml_eval():
	file = "testset.csv"
	test_file = pd.read_csv(file)

	r = NBTest.detecting(file)
	nb = model_assessment(test_file['sentiment'], r)
	print("NB Accuracy=", nb)

	r = SVMTest.detecting(file)
	svm = model_assessment(test_file['sentiment'], r)
	print("SVM Accuracy=", svm)

	r = NNTest.detecting(file)
	nn = model_assessment(test_file['sentiment'], r)
	print("NN Accuracy=", nn)

	r = RFTest.detecting(file)
	rf = model_assessment(test_file['sentiment'], r)
	print("RF Accuracy=", rf)


	database = DBConnection.getConnection()
	cursor = database.cursor()
	cursor.execute("delete from accuracy")
	cursor.execute("insert into accuracy values(" + str(nb) + "," + str(svm) + "," + str(nn) + "," + str(rf) + ")")
	database.commit()


	return nb, svm, nn, rf




#ml_eval()
