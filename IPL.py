
# coding: utf-8

# In[3]:
#libraries used
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as mlt
import seaborn as sns


# In[60]:
#reading the dataset files
matches=pd.read_csv('C:/Users/vrajm/Desktop/IPL/matches.csv') # read Matches file
matches.head(5) #print only the first 5 rows


# In[57]:

delivery=pd.read_csv('C:/Users/vrajm/Desktop/IPL/deliveries.csv') #read Delivery file
delivery.head(5) #print only the first 5 rows


# In[51]:

print ("Total number of matches played:", len(matches)) #finding the number of matches played in total
print(' \n Location for all matches: \n',matches['city'].unique(), ' \n \n Teams :',matches['team1'].unique(), '\n \nTotal umpires ',matches['umpire1'].unique()) #Location of Matches, name of teams that played and the name of unique umpires


# In[53]:

del matches['umpire3'] #remove the column with no data or consists of NaN


# In[55]:

matches.head(4) #Matches file after removing umpire3 column


# In[119]:

a= matches['player_of_match'].value_counts()
b= a.idxmax()

print(' Who has the highest man of the match awards?\n', b)

c= matches['winner'].value_counts()
d=c.idxmax()
print(' Which team has won the most?\n', d)

#a= matches['player_of_match'].value_counts().idxmax()
#print('Who has the highest man of the match awards?', a)
#print((matches['player_of_match'].value_counts()).idxmax(),' : has most man of the match awards')


# In[223]:

x=matches.iloc[[matches['win_by_runs'].idxmax()]]
x


# In[275]:

x=matches.iloc[[matches['win_by_runs'].idxmax()]]
print('It was in', x['season'].item(),',','when the biggest score difference was', x['win_by_runs'].item(), ',', 'between', x['team1'].item(), '&', x['team2'].item(),'.' , 
      ' ','The match was won by:', x['winner'].item())
#print(x['season'].item())


# In[286]:

q = matches['toss_decision'].value_counts()
q/len(matches)*100


# In[287]:

sns.countplot(x='season',hue='toss_decision',data=matches)
mlt.show()
#the graph will show the decision of fielding or batting if a team wins the toss. 


# In[304]:

u=matches['toss_winner'].value_counts().plot.bar()
for l in u.patches:
    u.annotate(format(l.get_height()), (l.get_x()+0.15, l.get_height()+1))
mlt.show()

#the graph shows the team that won the most tosses
#Mumbai Indians won the most toss


# In[305]:

u=pd.concat([matches['team1'],matches['team2']])
matches_played_byteams=u.value_counts().reset_index()
matches_played_byteams.columns=['Team','Total Matches']
matches_played_byteams['wins']=matches['winner'].value_counts().reset_index()['winner']
matches_played_byteams.set_index('Team')
matches_played_byteams.plot.bar()
mlt.show()


# In[ ]:



