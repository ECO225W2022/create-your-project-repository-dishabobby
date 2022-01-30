#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
pd.read_csv("fatal_encounters_dot_org.csv")


# The burden of fatal police violence is an urgent public health crisis in the USA. Mounting evidence shows that deaths at the hands of the police disproportionately impact people of certain races and ethnicities, pointing to systemic racism in policing [1]. Black Americans are killed at a much higher rate than White Americans. Most victims are young males between 20 and 40 years old says Washington Post [2].
# 
# In order to investigate the choice of intentional use of force by the police, I pose the research question, 'is there is a relationship between the race and age of the victim and the choice to use brutal force by the police'. Here, the outcome variable is the use of force and the two predictor variables are the race and, the age of the victim. 
# 
# For this analysis, I’ve used the Police Violence & Racial Equity — Part 1 of 3 data by JohnM on Kaggle. The police encounter data is collected between 2000 and 2010. 
# 

# References:
# 1. https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(21)01609-3/fulltext
# 2. https://www.washingtonpost.com/graphics/investigations/police-shootings-database/
