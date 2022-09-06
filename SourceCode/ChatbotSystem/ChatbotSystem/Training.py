from RFTrain import RFTrain
from SVMTrain import SVMTrain
from NBTrain import NBTrain
from NNTrain import NNTrain

file="Training.csv"

print("Random Forest Started")
r=RFTrain()
r.detecting(file)
print("Random Forest Completed")
print("Naive Bayes Started")
n=NBTrain()
n.detecting(file)
print("Naive Bayes Completed")
print("SVM Started")
#s=SVMTrain()
#s.detecting(file)
print("SVM Completed")
n=NNTrain()
n.detecting(file)
