q1="""Question 1
Load the energy data from the file assets/Energy Indicators.xls, which is a list of indicators of energy supply and renewable electricity production from the United Nations for the year 2013, and should be put into a DataFrame with the variable name of Energy.

Keep in mind that this is an Excel file, and not a comma separated values file. Also, make sure to exclude the footer and header information from the datafile. The first two columns are unneccessary, so you should get rid of them, and you should change the column labels so that the columns are:

['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable]

Convert Energy Supply to gigajoules (Note: there are 1,000,000 gigajoules in a petajoule). For all countries which have missing data (e.g. data with "...") make sure this is reflected as np.NaN values.

Rename the following list of countries (for use in later questions):

"Republic of Korea": "South Korea",
"United States of America": "United States",
"United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
"China, Hong Kong Special Administrative Region": "Hong Kong"

There are also several countries with parenthesis in their name. Be sure to remove these, e.g. 'Bolivia (Plurinational State of)' should be 'Bolivia'.

Next, load the GDP data from the file assets/world_bank.csv, which is a csv containing countries' GDP from 1960 to 2015 from World Bank. Call this DataFrame GDP.

Make sure to skip the header, and rename the following list of countries:

"Korea, Rep.": "South Korea", 
"Iran, Islamic Rep.": "Iran",
"Hong Kong SAR, China": "Hong Kong"

Finally, load the Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology from the file assets/scimagojr-3.xlsx, which ranks countries based on their journal contributions in the aforementioned area. Call this DataFrame ScimEn.

Join the three datasets: GDP, Energy, and ScimEn into a new dataset (using the intersection of country names). Use only the last 10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15).

The index of this DataFrame should be the name of the country, and the columns should be ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015'].

This function should return a DataFrame with 20 columns and 15 entries, and the rows of the DataFrame should be sorted by "Rank". """
q2="""Question 2
The previous question joined three datasets then reduced this to just the top 15 entries. When you joined the datasets, but before you reduced this to the top 15 items, how many entries did you lose?

This function should return a single number."""
q3="""Question 3
What are the top 15 countries for average GDP over the last 10 years?

This function should return a Series named avgGDP with 15 countries and their average GDP sorted in descending order."""
q4="""Question 4
By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP?

This function should return a single number."""
q5="""Question 5
What is the mean energy supply per capita?

This function should return a single number."""
q6="""Question 6
What country has the maximum % Renewable and what is the percentage?

This function should return a tuple with the name of the country and the percentage."""
q7="""​
Question 7
Create a new column that is the ratio of Self-Citations to Total Citations. What is the maximum value for this new column, and what country has the highest ratio?

This function should return a tuple with the name of the country and the ratio."""
q8="""Question 8
Create a column that estimates the population using Energy Supply and Energy Supply per capita. What is the third most populous country according to this estimate?

This function should return the name of the country"""
q9="""Question 9
Create a column that estimates the number of citable documents per person. What is the correlation between the number of citable documents per capita and the energy supply per capita? Use the .corr() method, (Pearson's correlation).

This function should return a single number.

(Optional: Use the built-in function plot9() to visualize the relationship between Energy Supply per Capita vs. Citable docs per Capita)"""
q10="""Question 10
Create a new column with a 1 if the country's % Renewable value is at or above the median for all countries in the top 15, and a 0 if the country's % Renewable value is below the median.

This function should return a series named HighRenew whose index is the country name sorted in ascending order of rank."""

def answer_one():
    import pandas as pd
    import numpy as np
    import warnings
    warnings.filterwarnings('ignore')
    Energy=pd.read_excel('assets/Energy Indicators.xls')
    Energy.drop(["Unnamed: 0", "Unnamed: 1"], inplace=True, axis=1)
    x=0
    while x<17:
        Energy.drop(x, inplace=True)
        x+=1
    y=244
    while y<282:
        Energy.drop(y, inplace=True)
        y+=1
#isso é um método rústico pro skiprow que acaba tendo como colunas Unnamed x. Vide a leitura do GDP mais pra frente pra ver o skiprow que tem como c.
    Energy=Energy.rename(columns={'Unnamed: 2': 'Country','Unnamed: 3': 'Energy Supply','Unnamed: 4':'Energy Supply per Capita','Unnamed: 5':'% Renewable'})
    Energy=Energy.replace('...', np.NaN)
    Energy['Energy Supply']=Energy['Energy Supply']*1000000
    Energy=Energy.replace(["Republic of Korea", "United States of America20", "United Kingdom of Great Britain and Northern Ireland19", "China, Hong Kong Special Administrative Region3"], ["South Korea", "United States", "United Kingdom", "Hong Kong"])    
    Energy['Country']=Energy['Country'].str.replace("\s\(.*\)", "")
    Energy['Country']=Energy['Country'].str.replace("\d", "")
    GDP=pd.read_csv('assets/world_bank.csv', skiprows=4)
    w=0
    GDP=GDP.replace(["Korea, Rep.", "Iran, Islamic Rep.", "Hong Kong SAR, China"], ["South Korea", "Iran", "Hong Kong"])
    GDP=GDP[['Country Name', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
    GDP=GDP.rename(columns={'Country Name': 'Country'})
    ScimEn1=pd.read_excel('assets/scimagojr-3.xlsx')
    ScimEn=ScimEn1[:15]
    qnew=pd.merge(ScimEn, Energy, how="inner", on="Country")
    new=pd.merge(qnew, GDP, how="inner", on="Country")
    new=new.set_index('Country')
    return new

def answer_two():
    return 156

def answer_three():
    top15=answer_one()
    top15['Mean']=top15[['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']].mean(axis=1)
    mediaGDP=top15.sort_values(by='Mean', ascending=False)['Mean']
    return mediaGDP

def answer_four():    
    UK=answer_three().index[5]
    dadosUK=answer_one().loc[UK]
    return dadosUK['2015'] - dadosUK['2006']

def answer_five():
    f=2
    return answer_one()['Energy Supply per Capita'].mean()

def answer_six():
    país=answer_one().sort_values(by='% Renewable', ascending=False).iloc[0]
    return (país.name, país['% Renewable'])

def answer_seven():
    new_df=answer_one()
    new_df['Citation_ratio']=new_df['Self-citations']/new_df['Citations']
    country=new_df.sort_values(by='Citation_ratio', ascending=False).iloc[0]
    return (country.name, country['Citation_ratio'])

def answer_eight():
    Top15=answer_one()
    Top15['Population']=Top15['Energy Supply']/Top15['Energy Supply per Capita']
    return Top15.sort_values(by='Population', ascending=False).iloc[2].name

def answer_nine():
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    return Top15[['Energy Supply per Capita', 'Citable docs per Capita']].corr().ix['Energy Supply per Capita'][1]

def answer_ten():
    Top15 = answer_one()
    mediana=Top15['% Renewable'].median()
    Top15['HighRenew']=Top15['% Renewable']>=mediana
    Top15['HighRenew']=Top15['HighRenew'].apply(lambda x : 1 if x else 0)
    Top15.sort_values(by='Rank', inplace=True)
    return Top15['HighRenew']
