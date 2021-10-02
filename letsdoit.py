import pandas as pd


df=read_csv("username.csv", sep=";")
df["age"]=''
for x in df.index:
  k=x
  
