import pandas as pd, sys
import csv


#these are residual from other methods I used
from bs4 import BeautifulSoup
import requests

f = open("D:\Stock market python-etc/first 498 NYSE symbols.csv", "r")

# Loop over each line/symbol name in the file.
for symbol in f.readlines():
    
    symbol = symbol.strip()
    #I ound out this allows "symbol" and ".csv" to be next to each other, same line. 

    old_filename = symbol +".csv"
    print(old_filename)
    
    # create new file name to work with, as well as preserve original 
    name_1 = "edited_"
    name_2 = symbol
    name_3 = ".csv"
    new_filename = name_1 + name_2 + name_3
    print(new_filename)

    #print old & new fie names to verify. This part works great 

    # here is where the problems start. I've used your method, and a couple others, all have the same "file not found" error
    df = pd.read_csv("(new_filename)")
    # note, I've also tried:
            #df = pd.read_csv("A.csv")   (an individual csv file)
            #df = pd.read_csv("7-31-19_downloads/A.csv") same file, including current folder
            #df = pd.read_csv("D:\Stock market python-etc\7-31-19_downloads/A.csv) same again including full path
            # as well as various combinations using single quotes, double quotes, and parenthesis

    # the  df function is where I have the problem. It keeps saying
    # "file not found", yet the files in question are in the same folder  
    
    df.head(3)

    break 
    
    
    # how to save new csv file
    # df.to_csv("new_filename")

    

    
