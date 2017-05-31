
# coding: utf-8

# In[1]:

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as mlt
import seaborn as sns
matches=pd.read_csv('C:/Users/vrajm/Desktop/IPL/matches.csv')   
delivery=pd.read_csv('C:/Users/vrajm/Desktop/IPL/deliveries.csv')
print ("Total number of matches played:", len(matches))
matches.drop(['umpire3'],axis=1,inplace=True)  #since all the values are NaN
delivery.fillna(0,inplace=True)     #filling all the NaN values with 0

