import glob
import os
import matplotlib as plt
import pandas as pd
import numpy as np
import seaborn as sns
import csv
import scipy.stats as stats
import pandas as pd
import statsmodels
from statsmodels.stats.descriptivestats import describe
import seaborn as sns
from pathlib import Path
#specifies the ammount of participants
number_of_files = 9
#Creates dataframe to insert results
dfObj = pd.DataFrame(columns=['Invalid Cue', 'Neutral Cue', 'Valid Cue', 'Incongruent', 'Congruent', 
                              'Valid Incongruent', 'Neutral Incongruent', 'Invalid Incongruent', 'Valid Congruent', 
                              'Neutral Congruent', 'Invalid Congruent', 'Gratton Congruent', 'Gratton Incongruent', 
                              'Gratton', 'Gratton Invalid', 'Gratton Neutral', 'Gratton Valid', 'Reactionavg'])
#Beggins the loop looking for the numbered .csv files 
for i in range(1, number_of_files+1):
    data = pd.read_csv("{}.csv".format(i))
    #Eliminates exceding rows from the csvs
    data = data[data['Reaction']<1.5]
    data = data[data['Reaction']>0.05]
    #Eliminate exceding rows if answers incorrect
    #carries out the filtering for gratton
    data['Gratton'] = (data['Congruency']==0).shift(1)
    Gratton = data.loc[(data['Gratton'] ==True), 'Reaction'].mean()
    Gratton1 = data.loc[(data['Gratton'] ==True) & data['Congruency'] == 1, 'Reaction'].mean()
    Gratton2 = data.loc[(data['Gratton'] ==True) & data['Congruency'] == 0, 'Reaction'].mean()
    Gratton3 = data.loc[(data['Gratton'] ==True) & (data['Cue'] == 4), 'Reaction'].mean() #INVALIDO RECUERDA
    Gratton4 = data.loc[(data['Gratton'] ==True) & (data['Cue'] == 3), 'Reaction'].mean()
    Gratton5 = data.loc[(data['Gratton'] ==True) & (data['Cue'] <= 2), 'Reaction'].mean() #VALIDO RECUERDA
    #creates new column for accuracy
    data['Accuracy'] = np.where(data['Target']==data['Response'], 1, 0)
    data = data[data['Accuracy']==1]
    #This is not very elegant but it provides the means to all the needed conditions
    reactionavg = data.loc[(data['Trial'] >= 0) , 'Reaction'].mean()
    reaction1 = data.loc[(data['Cue'] ==4), 'Reaction'].mean()
    reaction2 = data.loc[(data['Cue'] ==3), 'Reaction'].mean()
    reaction3 = data.loc[(data['Cue']<=2), 'Reaction'].mean()
    reaction4 = data.loc[(data['Congruency']==0), 'Reaction'].mean()
    reaction5 = data.loc[(data['Congruency']==1), 'Reaction'].mean()
    reaction6 = data.loc[(data['Cue'] <=2) & (data['Congruency']==0), 'Reaction'].mean()
    reaction7 = data.loc[(data['Cue'] ==3) & (data['Congruency']==0), 'Reaction'].mean()
    reaction8 = data.loc[(data['Cue'] ==4) & (data['Congruency']==0), 'Reaction'].mean()
    reaction9 = data.loc[(data['Cue'] <=2) & (data['Congruency']==1), 'Reaction'].mean()
    reaction10 = data.loc[(data['Cue'] ==3) & (data['Congruency']==1), 'Reaction'].mean()
    reaction11 = data.loc[(data['Cue'] ==4) & (data['Congruency']==1), 'Reaction'].mean()
    #Assigns all the results to the appropiate columns in the pre-created dataframe
    dfObj = dfObj.append({'Invalid Cue': reaction1, 'Neutral Cue': reaction2, 'Valid Cue': reaction3, 'Incongruent': reaction4 , 
                         'Congruent':reaction5 , 'Valid Incongruent':reaction6 , 'Neutral Incongruent':reaction7 , 
                         'Invalid Incongruent':reaction8 , 'Valid Congruent':reaction9 , 'Neutral Congruent':reaction10 , 
                         'Invalid Congruent':reaction11,'Gratton Congruent': Gratton1, 'Gratton Incongruent': Gratton2, 
                         'Gratton': Gratton, 'Gratton Invalid': Gratton3 , 'Gratton Neutral': Gratton4 , 'Gratton Valid': Gratton5, 
                         'Reactionavg':reactionavg }, ignore_index=True)
    #calculates the differences
    dfObj['Valid difference'] = dfObj['Valid Incongruent']-dfObj['Valid Congruent']
    dfObj['Neutral difference'] = dfObj['Neutral Incongruent']-dfObj['Neutral Congruent']
    dfObj['Invalid difference'] = dfObj['Invalid Incongruent']-dfObj['Invalid Congruent']
    dfObj['Flanker'] = dfObj['Incongruent']-dfObj['Congruent']
#This just prints the content everytime with the titlecard Dataframe Contents 
print("Dataframe Contents", dfObj, sep='\n')
print(data)
#this would be to check on the last operated data but not needed unless something went horribly wrong
#this to check only correct responses have been included, if so, it will be 1
data["Accuracy"].mean()
#print(dfObj)
#same as previous code line

import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid") #Cause aesthetics matter
sns.set(rc={'figure.figsize':(11.7,8.27)})

# an example on how to set limits plt.ylim(5, 45)

#select for individual plots, you gotta look how to make it so that all are independently made --- spacing didnt work
#not good plot examples, sets them as the y axis
#DO NOT USE BUT KEEP TO REMEMBER
#sns.violinplot(x=dfObj["Invalid Cue"])
#sns.violinplot(x=dfObj["Neutral Cue"]

#Plots per cue
sns.violinplot(data=dfObj[["Invalid Cue", "Neutral Cue", "Valid Cue"]])
plt.ylim(0.2, 1.2)

#Plots per congruency
sns.violinplot(data=dfObj[["Incongruent", "Congruent"]])
plt.ylim(0.2, 1.2)           
#Plots per combined incongruent
sns.violinplot(data=dfObj[["Valid Incongruent", "Neutral Incongruent", "Invalid Incongruent"]])
plt.ylim(0.2, 1.2)
#Plots per combined congruent
sns.violinplot(data=dfObj[["Valid Congruent", "Neutral Congruent", "Invalid Congruent"]])
plt.ylim(0.2, 1.2)




sns.violinplot(data=dfObj[["Gratton Congruent", "Congruent"]])
plt.ylim(0.3, 1)  

sns.violinplot(data=dfObj[["Gratton Incongruent", "Incongruent"]])
plt.ylim(0.3, 1) 

sns.violinplot(data=dfObj[["Gratton Invalid", "Invalid Cue"]])
plt.ylim(0.3, 1)

sns.violinplot(data=dfObj[["Gratton Neutral", "Neutral Cue"]])
plt.ylim(0.3, 1) 

sns.violinplot(data=dfObj[["Gratton Valid", "Valid Cue"]])
plt.ylim(0.3, 1) 

sns.violinplot(data=dfObj[["Gratton", "Reactionavg"]])
plt.ylim(0.3, 1) 
 



sns.violinplot(data=dfObj[["Valid Congruent", "Neutral Congruent", "Invalid Congruent", "Valid Incongruent", "Neutral Incongruent", "Invalid Incongruent"]])
plt.ylim(0.2, 1.1)

#Creates flanker column (Maybe move this up with the loop before the rest of the graphs?)
#dfObj['Flanker'] = dfObj['Incongruent']-dfObj['Congruent']

print(dfObj)

describe(dfObj["Invalid Cue"])
describe(dfObj["Valid Cue"])
describe(dfObj["Neutral Cue"])

describe(dfObj["Congruent"])
describe(dfObj["Incongruent"])

describe(dfObj["Valid Incongruent"])
describe(dfObj["Neutral Incongruent"])
describe(dfObj["Invalid Incongruent"])

describe(dfObj["Valid Congruent"])
describe(dfObj["Neutral Congruent"])
describe(dfObj["Invalid Congruent"])

describe(dfObj["Valid difference"])
describe(dfObj["Neutral difference"])
describe(dfObj["Invalid difference"])

describe(dfObj["Gratton"])
describe(dfObj["Gratton Congruent"])
describe(dfObj["Gratton Incongruent"])

describe(dfObj["Gratton Invalid"])
describe(dfObj["Gratton Neutral"])
describe(dfObj["Gratton Valid"])

describe(dfObj["Reactionavg"])

#sns.violinplot(y="Flanker", data=dfObj)
#This plot is just dumb

#sns.violinplot(data=dfObj[["Incongruent", "Congruent", "Flanker"]])
#This one feels even dumber


#dfObj['Valid difference'] = dfObj['Valid Incongruent']-dfObj['Valid Congruent']
#dfObj['Neutral difference'] = dfObj['Neutral Incongruent']-dfObj['Neutral Congruent']
#dfObj['Invalid difference'] = dfObj['Invalid Incongruent']-dfObj['Invalid Congruent']

sns.violinplot(data=dfObj[["Valid difference", "Neutral difference", "Invalid difference"]])


describe(data)
describe(dfObj)

stats.ttest_ind(dfObj["Incongruent"],
                dfObj["Congruent"])

stats.ttest_ind(dfObj["Gratton"],
                dfObj["Reactionavg"])

stats.ttest_ind(dfObj["Gratton Congruent"],
                dfObj["Congruent"])

stats.ttest_ind(dfObj["Gratton Incongruent"],
                dfObj["Incongruent"])

stats.ttest_ind(dfObj["Gratton Invalid"],
                dfObj["Invalid Cue"])

stats.ttest_ind(dfObj["Gratton Neutral"],
                dfObj["Neutral Cue"])

stats.ttest_rel(dfObj['Incongruent'], dfObj['Congruent'])


import statsmodels.api as sm
from statsmodels.formula.api import ols

#perform two-way ANOVA
model = ols('Reaction ~ C(Congruency) + C(Flanker) + C(Congruency):C(Flanker)', data=data).fit()
sm.stats.anova_lm(model, typ=2)

from scipy.stats import f_oneway
f_oneway(dfObj["Congruent"], dfObj["Incongruent"])
f_oneway(dfObj["Invalid Cue"], dfObj["Neutral Cue"], dfObj["Valid Cue"])
f_oneway(dfObj["Invalid Congruent"], dfObj["Invalid Incongruent"], dfObj["Neutral Congruent"], dfObj["Neutral Incongruent"], dfObj["Valid Congruent"],  dfObj["Valid Incongruent"])
f_oneway(dfObj["Invalid Incongruent"], dfObj["Neutral Incongruent"],dfObj["Valid Incongruent"])
f_oneway(dfObj["Invalid Congruent"], dfObj["Neutral Congruent"], dfObj["Valid Congruent"])
f_oneway(dfObj["Valid difference"], dfObj["Neutral difference"],dfObj["Invalid difference"])







folder = 'C:/Users/ADM20/Desktop/Master project/drive-download-20220330T171320Z-001/'

#This is to know what files are in the folder and create a list
# ext = ('.csv')
# for files in os.scandir():
#     if files.path.endswith(ext):
#         print(files)

#Sets the number of operations based on number of participants - set manually
number_of_files = 9

#Creates dataframe to insert results
dfObj = pd.DataFrame(columns=['Invalid Cue', 'Neutral Cue', 'Valid Cue', 'Incongruent', 'Congruent', 'Valid Incongruent', 'Neutral Incongruent', 'Invalid Incongruent', 'Valid Congruent', 'Neutral Congruent', 'Invalid Congruent'])

#Beggins the loop looking for the numbered .csv files 
for i in range(1, number_of_files+1):
    data = pd.read_csv("{}.csv".format(i))
    
    #Eliminates exceding rows from the csvs
    data = data[data['Reaction']<1.5]
    data = data[data['Reaction']>0.05]
    #Eliminate exceding rows if answers incorrect
    
    
    #creates new column for accuracy
    data['Accuracy'] = np.where(data['Target']==data['Response'], 1, 0)
    #data = data[data['Accuracy']==1]
    
    #This is not very elegant but it provides the means to all the needed conditions
    Accuracy1 = data.loc[(data['Cue'] ==4), 'Accuracy'].mean()
    Accuracy2 = data.loc[(data['Cue'] ==3), 'Accuracy'].mean()
    Accuracy3 = data.loc[(data['Cue']<=2), 'Accuracy'].mean()
    Accuracy4 = data.loc[(data['Congruency']==0), 'Accuracy'].mean()
    Accuracy5 = data.loc[(data['Congruency']==1), 'Accuracy'].mean()
    Accuracy6 = data.loc[(data['Cue'] <=2) & (data['Congruency']==0), 'Accuracy'].mean()
    Accuracy7 = data.loc[(data['Cue'] ==3) & (data['Congruency']==0), 'Accuracy'].mean()
    Accuracy8 = data.loc[(data['Cue'] ==4) & (data['Congruency']==0), 'Accuracy'].mean()
    Accuracy9 = data.loc[(data['Cue'] <=2) & (data['Congruency']==1), 'Accuracy'].mean()
    Accuracy10 = data.loc[(data['Cue'] ==3) & (data['Congruency']==1), 'Accuracy'].mean()
    Accuracy11 = data.loc[(data['Cue'] ==4) & (data['Congruency']==1), 'Accuracy'].mean()

    #Assigns all the results to the appropiate columns in the pre-created dataframe
    dfObj = dfObj.append({'Invalid Cue': Accuracy1, 'Neutral Cue': Accuracy2, 'Valid Cue': Accuracy3, 'Incongruent': Accuracy4 , 
                         'Congruent':Accuracy5 , 'Valid Incongruent':Accuracy6 , 'Neutral Incongruent':Accuracy7 , 'Invalid Incongruent':Accuracy8 , 'Valid Congruent':Accuracy9 , 'Neutral Congruent':Accuracy10 , 'Invalid Congruent':Accuracy11 }, ignore_index=True)
    
    dfObj['Flanker'] = dfObj['Incongruent']-dfObj['Congruent']
    
#This just prints the content everytime with the titlecard Dataframe Contents 
print("Dataframe Contents", dfObj, sep='\n')
    
print(data)
#this would be to check on the last operated data but not needed unless something went horribly wrong
#this to check only correct responses have been included, if so, it will be 1
data["Accuracy"].mean()
#print(dfObj)
#same as previous code line

import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid") #Cause aesthetics matter
sns.set(rc={'figure.figsize':(11.7,8.27)})

# an example on how to set limits plt.ylim(5, 45)

#select for individual plots, you gotta look how to make it so that all are independently made --- spacing didnt work
#not good plot examples, sets them as the y axis
#DO NOT USE BUT KEEP TO REMEMBER
#sns.violinplot(x=dfObj["Invalid Cue"])
#sns.violinplot(x=dfObj["Neutral Cue"])

#Example of functioning plot
sns.violinplot(y="Congruent", data=dfObj)

#Plots per cue
sns.violinplot(data=dfObj[["Invalid Cue", "Neutral Cue", "Valid Cue"]])
plt.ylim(0.6, 1.2)

#Plots per congruency
sns.violinplot(data=dfObj[["Incongruent", "Congruent"]])
plt.ylim(0.6, 1.2)           
#Plots per combined incongruent
sns.violinplot(data=dfObj[["Valid Incongruent", "Neutral Incongruent", "Invalid Incongruent"]])
plt.ylim(0.6, 1.2)
#Plots per combined congruent
sns.violinplot(data=dfObj[["Valid Congruent", "Neutral Congruent", "Invalid Congruent"]])
plt.ylim(0.6, 1.2)


sns.violinplot(data=dfObj[["Valid Congruent", "Neutral Congruent", "Invalid Congruent", "Valid Incongruent", "Neutral Incongruent", "Invalid Incongruent"]])
plt.ylim(0.6, 1.2)

#Creates flanker column (Maybe move this up with the loop before the rest of the graphs?)
dfObj['Flanker'] = dfObj['Incongruent']-dfObj['Congruent']

print(dfObj)

#sns.violinplot(y="Flanker", data=dfObj)
#This plot is just dumb

#sns.violinplot(data=dfObj[["Incongruent", "Congruent", "Flanker"]])
#This one feels even dumber


dfObj['Valid difference'] = dfObj['Valid Incongruent']-dfObj['Valid Congruent']
dfObj['Neutral difference'] = dfObj['Neutral Incongruent']-dfObj['Neutral Congruent']
dfObj['Invalid difference'] = dfObj['Invalid Incongruent']-dfObj['Invalid Congruent']

sns.violinplot(data=dfObj[["Valid difference", "Neutral difference", "Invalid difference"]])


describe(dfObj["Invalid Cue"])
describe(dfObj["Valid Cue"])
describe(dfObj["Neutral Cue"])

describe(dfObj["Congruent"])
describe(dfObj["Incongruent"])

describe(dfObj["Valid Incongruent"])
describe(dfObj["Neutral Incongruent"])
describe(dfObj["Invalid Incongruent"])


describe(dfObj["Valid Congruent"])
describe(dfObj["Neutral Congruent"])
describe(dfObj["Invalid Congruent"])


#now we have to carry out the usual statistical analyses
#independent samples t-test?
#pearsons R?

for i in range(1, number_of_files+1):
    data = pd.read_csv("{}.csv".format(i))
    
    #Eliminates exceding rows from the csvs
    data = data[data['Reaction']<1.5]
    data = data[data['Reaction']>0.05]
    #Eliminate exceding rows if answers incorrect
    
    
    #creates new column for accuracy
    data['Accuracy'] = np.where(data['Target']==data['Response'], 1, 0)

import pandas as pd
import scipy.stats as stats

print(data)
pearsonr(data['Reaction'], data['Accuracy'])
describe(data)
stats.ttest_ind(dfObj["Incongruent"],
                dfObj["Congruent"])

from scipy.stats import f_oneway
f_oneway(dfObj["Congruent"], dfObj["Incongruent"])
f_oneway(dfObj["Invalid Cue"], dfObj["Neutral Cue"], dfObj["Valid Cue"])
f_oneway(dfObj["Invalid Congruent"], dfObj["Invalid Incongruent"], dfObj["Neutral Congruent"], dfObj["Neutral Incongruent"], dfObj["Valid Congruent"],  dfObj["Valid Incongruent"])


stats.ttest_ind(dfObj["Incongruent"],
                dfObj["Congruent"])

stats.ttest_ind(dfObj["Gratton"],
                dfObj["Reactionavg"])

stats.ttest_ind(dfObj["Gratton Congruent"],
                dfObj["Congruent"])

stats.ttest_ind(dfObj["Gratton Incongruent"],
                dfObj["Incongruent"])

stats.ttest_ind(dfObj["Gratton Invalid"],
                dfObj["Invalid Cue"])

stats.ttest_ind(dfObj["Gratton Neutral"],
                dfObj["Neutral Cue"])

stats.ttest_rel(dfObj['Incongruent'], dfObj['Congruent'])


import statsmodels.api as sm
from statsmodels.formula.api import ols

#perform two-way ANOVA
model = ols('Reaction ~ C(Congruency) + C(Flanker) + C(Congruency):C(Flanker)', data=data).fit()
sm.stats.anova_lm(model, typ=2)

from scipy.stats import f_oneway
f_oneway(dfObj["Congruent"], dfObj["Incongruent"])
f_oneway(dfObj["Invalid Cue"], dfObj["Neutral Cue"], dfObj["Valid Cue"])
f_oneway(dfObj["Invalid Congruent"], dfObj["Invalid Incongruent"], dfObj["Neutral Congruent"], dfObj["Neutral Incongruent"], dfObj["Valid Congruent"],  dfObj["Valid Incongruent"])
f_oneway(dfObj["Invalid Incongruent"], dfObj["Neutral Incongruent"],dfObj["Valid Incongruent"])
f_oneway(dfObj["Invalid Congruent"], dfObj["Neutral Congruent"], dfObj["Valid Congruent"])
f_oneway(dfObj["Valid difference"], dfObj["Neutral difference"],dfObj["Invalid difference"])

    
    
