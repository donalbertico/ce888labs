import numpy as np
import sklearn
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("bank-additional-full.csv", delimiter=";")

data_dummies = pd.get_dummies(data)
del data_dummies["duration"]
del data_dummies["y_no"]



from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import train_test_split
xdata = data_dummies.iloc[:,0:-1]
ydata = data_dummies.iloc[:,-1]

xtrain, xtest, ytrain, ytest = train_test_split(xdata,ydata, test_size=0.3, random_state=100)

clf = ExtraTreesClassifier(n_estimators=100)
clf.fit(xdata,ydata)
