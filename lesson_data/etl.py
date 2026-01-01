import pandas as ps

cities=['Rabat','Casa','Marrakeche','Tanger','Fes','Agadir']
temperatures=[19,18,10,20,13,23]
df=ps.DataFrame({'City':cities,'Temp':temperatures})
"""
    2- Transformation
"""
# Normalisation
#creteria=df['Temp'] == NaN
df['Matche']=[2,1,0,1,1,0]
df.loc[len(df)]=['Rabat',17,None]
df['Temp']=df['Temp'].median()
#print(df)
df.fillna(0,inplace=True)
df.drop_duplicates(subset='City',inplace=True,keep='last')
print(df)
"""
    1- Extraction

# Projection : SELECT City FROM T

s_city=df['City']
print(s_city)
# SELECT AVG(Temp) FROM T
print(df['Temp'].mean(),df['Temp'].median())
#add Column
df['Matche']=[2,1,0,1,1,0]
print(df)
# SELECT City FROM T WHERE Matche 1= 0
print(df[df['Matche'] != 0]['City'])
# SELECT * FROM T WHERE Matche != 0 AND Temp >=20
creteria=(df['Matche'] != 0) & (df['Temp'] >= 20)
print(df[creteria])
row=df.loc[0]
print(df.loc[:3])
#Add row (append)
import numpy as np
df.loc[len(df)]=[None,17,np.nan]
print(df)
# SELECT City, Temp FROM T WHERE Temp < 19 AND Matches != 0
mask=(df['Matche'] != 0) & (df['Temp'] < 19)
print(df.loc[mask,['City','Temp']])
# SELECT City, Temp FROM T WHERE Temp < 19 AND Matches != 0 ODER BY Temp
print(df.loc[mask,['City','Temp']].sort_values(by='Temp',ascending=False))
# SELECT * FROM T WHERE City LIKE %s%

new_df=df.dropna()
filter =new_df['Temp'].astype(str).str.contains('^(2)',case=False)
print(new_df.loc[filter])
"""

"""
    0- Description

#description du dataSet
print(df)
#rows and columns
print(df.shape)
#size of df
print(len(df))
#information about dataset
print(df.info())
print(df.dtypes)
print(df.head(1))
print(df.tail(1))
#deescription statistique
print(df.describe()) """