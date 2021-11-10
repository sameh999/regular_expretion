from pandas.core.frame import DataFrame
import pandas as pd 
import numpy as np
import random as rd 
import re 

book = pd.read_csv(r"https://www.gutenberg.org/cache/epub/66309/pg66309.txt",sep="\t")
# get column of data frame of book
col =book.columns
# change the column name in book to cane work on it 
book.columns=["A"]
#variable to divide book to partitions 
partition = []
#variable to collect the partitions 
all_partitions =[]
#variable lapels all  partitions 
title = []
#counter to count lapels 
lapel =0
# counter to check that partition is 100 word 
count=0
# loop to divide the book to partations and collect partation in list 
for i in range(0 ,len(book)):
  #count words
  for line in book["A"][i].split(r' '):
    count =count +1
  #add word to partitions 
  partition.append(book["A"][i])
  #check if number of word more than 100 or not 
  if( count >= 120 ):
    # cleanning data from any special character
    d = re.sub('[^A-Za-z0-9\s]+', '', str(partition))
    #collect all partition to list  
    all_partitions.append(d )
    # make a title for evry partition in dataframe 
    lapel+= 1
    s = "partition " +str(lapel)
    #add lapel to title
    title.append(s )
    #clear counter to start again 
    count =0
    #clear partition  to start again 
    partition.clear() 
#collect all partition in data frame and and label the rows and coulmn 
df = pd.DataFrame(all_partitions, index =title,columns =[col])
# print the data frame of all partitions 
print(df)

