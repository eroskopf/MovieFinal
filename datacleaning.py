import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#need to import the files
f = open("./data/the_oscar_award.csv",'r')
oscar_winners = pd.read_csv(f)
#print(oscar_winners.head())

f2 = open("./data/oscar_movies.csv",'r')
movies = pd.read_csv(f2)
#print(movies.head())

f3 = open("./data/IMDB_movies.csv")
im = pd.read_csv(f3)
#print(im.head())

full = pd.merge(im, movies, on = "Film ID")
#print(full.iloc[1].get("Unnamed: 0_y"))
#print(full.iloc[1].get("Unnamed: 0_x"))
full = full.drop("Film_y", axis = 1)
full = full.drop("Unnamed: 0_y", axis = 1)
full = full.drop("Unnamed: 0_x", axis = 1)
print(full.head())
print(full.columns)

f4 = open("./data/movies.csv")
mov_rev = pd.read_csv(f4)
print(mov_rev.head())

full = pd.merge(full, mov_rev, how= 'left', left_on= ["Film_x", "Year of Release"], right_on=["name", "year"])
print(full.head())
print(full.loc[:,"budget"].isna())
full.to_csv(r"./data/fulldata.csv", index=False)

