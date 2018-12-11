from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import numpy as np
import pandas as pd

def main():
    pass

def readData():
    csv = pd.read_csv(FILEPATH)

def preprocessData(csv_data):
    #todo:
        #1 readData
        #2 Encode all categorical/string values to numerical
        #3 normalize data
        #4 split in train and test set
    pass

def createRandomForest():
    clf_rf = RandomForestClassifier(n_estimators=100)

def trainRandomForest():
    clf_rf.fit(TRAIN_DATA)

def predictRandomForest():
    clf_rf.predict(TEST_DATA)

def createSvc():
    clf_svc = SVC()

def trainSvc():
    clf_svc.fit(TRAIN_DATA)

def predictSvc():
    clf_svc.predict(TEST_DATA)

main()