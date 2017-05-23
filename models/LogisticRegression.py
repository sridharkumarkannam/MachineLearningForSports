import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn import linear_model
from sklearn.utils import shuffle

path = "/Users/Lai/Dropbox/PersonalProject/MachineLearningForSports/database/"

datas = ["atp_matches_1997.csv", "atp_matches_1998.csv", "atp_matches_1999.csv", "atp_matches_2000.csv", "atp_matches_2001.csv",
"atp_matches_2002.csv", "atp_matches_2003.csv", "atp_matches_2004.csv", "atp_matches_2005.csv", "atp_matches_2006.csv", "atp_matches_2007.csv", "atp_matches_2008.csv",
"atp_matches_2009.csv", "atp_matches_2010.csv", "atp_matches_2011.csv", "atp_matches_2012.csv", "atp_matches_2013.csv", "atp_matches_2014.csv", "atp_matches_2015.csv",
"atp_matches_2016.csv", "atp_matches_2017.csv"]




def read_dataframe(name):
	return pd.read_csv(name)

def concatenate_data(datas):
	dfs = []
	for data in datas:
		df = read_dataframe(path + data)
		dfs.append(df)
	return pd.concat(dfs)



# standardize our input data

def find_maximum_feature(x):
	return np.amax(x, axis=0)

def standardized(x):
	ymax = find_maximum_feature(x)
	ymin = np.amin(x,axis=0)
	return np.divide(x-ymin,ymax-ymin)


if __name__ == "__main__":

	# data preparation

	file = path + "try.csv"
	dataFile = read_dataframe(file)
	dataFileall = concatenate_data(datas)
	loser_on_court = np.array(dataFile.loser_on_court)
	winner_on_court = np.array(dataFile.winner_on_court)
	winning_ratio = np.array(dataFile.winning_ratio)
	winner_age = np.array(dataFileall.winner_age)
	loser_age = np.array(dataFileall.loser_age)
	winner_rank = np.array(dataFileall.winner_rank)
	loser_rank = np.array(dataFileall.loser_rank)
	rank_d = winner_rank - loser_rank





	winner_input = np.array([winner_age,winner_on_court,loser_age,loser_on_court,winning_ratio, rank_d])
	loser_input = np.array([loser_age,loser_on_court,winner_age,winner_on_court,1 - winning_ratio, -rank_d])

	winner_input = winner_input.T
	loser_input = loser_input.T

	winner_input = winner_input[~np.isnan(winner_input).any(axis=1)]
	loser_input = loser_input[~np.isnan(loser_input).any(axis=1)]
	winning_prediction = np.ones(len(winner_input[:,0])).reshape(len(winner_input[:,0]),1)
	losing_prediction = np.zeros(len(loser_input[:,0])).reshape(len(loser_input[:,0]),1)

	standardized_winner_input = standardized(winner_input)
	standardized_loser_input = standardized(loser_input)


	input = np.vstack((standardized_winner_input,standardized_loser_input))
	prediction = np.vstack((winning_prediction,losing_prediction)).reshape(2*len(loser_input[:,0]),)





	#train model


	input,prediction = shuffle(input,prediction,random_state=14)

	trainX, testX, trainY, testY = train_test_split(input, prediction, test_size = 0.5, random_state = 42)

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
















