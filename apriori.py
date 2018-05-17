# Apriori

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data Preprocessing
dataset = pd.read_csv('output.csv', header = None)
transactions = []
for i in range(0, 793):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 370)])
    

itens = []
for i in range(0, len(transactions)):
    itens.extend(transactions[i])
    
    
uniqueItems = list(set(itens))
uniqueItems.remove('nan')

pair = []
for j in range(0, len(uniqueItems)):
    k = 1;
    while k <= len(uniqueItems):
        try:
            pair.append([uniqueItems[j], uniqueItems[j+k]])
        except IndexError:
            pass
        k = k + 1;
        

# Creating trios# Creati 
trio = []
for j in range(0, len(uniqueItems)):
    for k in range(j, len(uniqueItems)):
        for l in range(k, len(uniqueItems)):
            if (k != j) and (j != l) and (k != l):
                try:
                    trio.append([uniqueItems[j], uniqueItems[j+k], uniqueItems[j+l]])
                except IndexError:
                    pass
                

score_trio = []
for i in pair:
    cond = []
    for item in i:
        cond.append("%s' in s" %item)
    mycode = ('[s for s in transactions if ' + ' and '.join(cond) + ']')
    #mycode = "print 'hello world'"
    score_trio.append(len(eval(mycode))/793.)