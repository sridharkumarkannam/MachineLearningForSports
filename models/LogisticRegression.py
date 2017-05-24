import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn import linear_model
from sklearn.utils import shuffle
import DataPrepare as dp




if __name__ == "__main__":



	data = dp.dataPrepare(dp.datas, dp.path)
	trainX = data[0]
	testX = data[1]  # a matrix
	trainY = data[2]  # a vector with binary number
	testY = data[3]

	clf = linear_model.SGDClassifier(loss="log")
	clf.fit(trainX,trainY)
	print(clf.fit(trainX,trainY))
	print(clf.coef_)
	print(clf.intercept_)



	#Now we will test our model

	pred_labels = clf.predict(testX)
	print(pred_labels)



	corrected_pred = 0
	for i in range(len(testX)):
		if pred_labels[i] == testY[i]:
			corrected_pred += 1
	print(corrected_pred/len(testY))
















