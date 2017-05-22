import pandas as pd
import numpy as np
datas = ["atp_matches_1997.csv", "atp_matches_1998.csv", "atp_matches_1999.csv", "atp_matches_2000.csv", "atp_matches_2001.csv", 
"atp_matches_2002.csv", "atp_matches_2003.csv", "atp_matches_2004.csv", "atp_matches_2005.csv", "atp_matches_2006.csv", "atp_matches_2007.csv", "atp_matches_2008.csv",
"atp_matches_2009.csv", "atp_matches_2010.csv", "atp_matches_2011.csv", "atp_matches_2012.csv", "atp_matches_2013.csv", "atp_matches_2014.csv", "atp_matches_2015.csv",
"atp_matches_2016.csv", "atp_matches_2017.csv"]


def read_dataframe(name):
	return pd.read_csv(name)

def concatenate_data(datas):
	dfs = []
	for data in datas:
		df = read_dataframe(data)
		dfs.append(df)
	return pd.concat(dfs)

""" 
Calculate the winner ratio over a specific court
1: for clay
2: grass
3: 
"""
def winner_over_surface(surface, player, date, dataFrame):
	new_df = dataFrame[dataFrame.tourney_date < date]
	win = new_df[new_df.winner_id == player]
	lose = new_df[new_df.loser_id == player]
	count_win = win.tourney_id[win.surface == surface].count()
	count_lose = lose.tourney_id[lose.surface == surface].count()
	if not (count_win + count_lose) == 0:
            return float(count_win)/float(count_win + count_lose)
        else:
            return 0

def head_to_head(playerA, playerB, date, dataFrame):
    new_df = dataFrame[dataFrame.tourney_date < date]
    Awon = new_df[new_df.winner_id == playerA]
    Bwon = new_df[new_df.winner_id == playerB]
    count_BlA = Awon.tourney_id[Awon.loser_id == playerB].count()
    count_AlB = Bwon.tourney_id[Bwon.loser_id == playerA].count()
    if (count_BlA + count_AlB) != 0:
        return float(count_BlA)/float(count_BlA + count_AlB)
    else:
        return 0

if __name__ == __main__:
	Clay = []
	Grass = []
	Hard = []
	Carpet = []
	A = []
	B = []
	C = []
	D = []
	winner_on_court = []
	loser_on_court = []
	winning_ratio = []

for i in range(df.tourney_id.count())
    for i in curdf.tourney_date:
        #print i
        date = i
    for j in curdf.winner_id:
        #print j
        wid = j
    for k in curdf.loser_id:
        #print k
        lid = k
    for s in curdf.surface:
        #print s
        sur = s
    winner = winner_over_surface(sur, wid, date, df)
    #print winner
    loser = winner_over_surface(sur, lid, date, df)
    winning_r = head_to_head(wid, lid, date, df)
    #print winning_r
    winner_on_court.append(winner)
    loser_on_court.append(loser)
    winning_ratio.append(winning_r)