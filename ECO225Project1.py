#!/usr/bin/env python
# coding: utf-8

# The burden of fatal police violence is an urgent public health crisis in the USA. Mounting evidence shows that deaths at the hands of the police disproportionately impact people of certain races and ethnicities, pointing to systemic racism in policing [1]. Black Americans are killed at a much higher rate than White Americans. Most victims are young males between 20 and 40 years old says Washington Post [2].
# 
# In order to investigate the choice of intentional use of force by the police, I pose the research question, 'is there is a relationship between the race and age of the victim and the choice to use brutal force by the police'. Here, the outcome variable is the use of force and the two predictor variables are the race and, the age of the victim. 
# 
# According to the National Institue of Justice, "broadly speaking, the use of force by law enforcement officers becomes necessary and is permitted under specific circumstances" [3]. In order to understand this analysis, it is important to define the "intentional use of force". The police force, in training, are taught 5 levels of force [4]. The first two levels are non-physical. The last three levels - "empty hand control", "non-lethal" and "lethal" are physical.
# 
# For this analysis, I’ve used the Police Violence & Racial Equity — Part 1 of 3 data by JohnM on Kaggle. The police encounter data is collected between 2000 and 2010. The dataset I use in my analysis is one of three that pull together data from several different sources related to police violence and racial equity in the United States. 
# 

# References:
# 1. https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(21)01609-3/fulltext
# 2. https://www.washingtonpost.com/graphics/investigations/police-shootings-database/
# 3. https://nij.ojp.gov/topics/law-enforcement/use-of-force
# 4. https://www.kaggle.com/jpmiller/police-violence-in-the-us

# In[2]:


import pandas as pd
csv= pd.read_csv("fatal_encounters_dot_org.csv")

df = pd.DataFrame(csv)


# The Y variable, use of intentional force, can be explained by two X variables - race of the victim and age of the victim. 

# In[3]:


#Cleaning the dataset to remove any rows with missing data values in columns containing the X and Y values
newdf = df.filter(["Subject's age", "Subject's race","Intentional Use of Force (Developing)"], axis=1)
cleandf1 = newdf[newdf["Subject's age"].notna()]
cleandf2 = cleandf1[cleandf1["Subject's race"].notna()]


# In[13]:


#Summary Statistics
cleandf2.describe()


# In[14]:


#Summary statistics
cleandf2.agg({
    "Subject's age": ["min", "max"]
})


# In[23]:


cleandf2["Intentional Use of Force (Developing)"].hist(by=cleandf2["Subject's race"])


# In[ ]:




