from __future__ import print_function

# coding: utf-8

# In[1]:

#get_ipython().magic(u'matplotlib notebook')
from matplotlib import pyplot as plt
import json
from collections import Counter
from datetime import datetime
import pandas as pd
import numpy as np


# In[2]:

# Sentiment Intensity Analyzer Using Vader
#from __future__ import print_function
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
sid = SentimentIntensityAnalyzer()

with open ("test5000.json") as f:#"yelp_dataset_challenge_round9/yelp_academic_dataset_review.json") as f:
    #comma delimited json requires read_json method to set lines parameter to true
    df = pd.read_json(json.loads(json.dumps(f.read())), lines=True)
    #list unique business IDS and user ids to construct full dataframe
    users = df.user_id.unique()
    businesses = df.business_id.unique()
    utility_matrix = pd.DataFrame(index=users, columns=businesses)
#print(utility_matrix)
print("business count ",len(utility_matrix.columns))
print("user count ", len(utility_matrix.index))


# In[4]:

#print(df.columns)
#print(utility_matrix)
for index, row in df.iterrows():
    compound_polarity_score = sid.polarity_scores(row['text'])
    user_id = row['user_id']
    business_id = row['business_id']
    utility_matrix[business_id][user_id] = compound_polarity_score['compound']
print(utility_matrix.columns,"summary: ",len(utility_matrix))
print(utility_matrix.index,"rows")
print(utility_matrix)


# In[ ]:

#A function that will take two user vectors and identify business_id that both users have reviewed
#should take in two pandas series objects and return a similarity 
#def calculate_cosine_similarity():
    
    


# In[68]:

#find top n most similar users to produce k recommended items
#first user is
first_user = utility_matrix.index[0]
#this is how you get the user vector 
first_user_prefs = utility_matrix.iloc[0,:]
second_user_prefs = utility_matrix.iloc[1,:]

#print(first_user_prefs)
#print(second_user_prefs)
# should euclidean distance be used for user profiles with only one rating?
index = 0
for rating in second_user_prefs:
    print(rating, index, first_user_prefs, second_user_prefs)
    index+=1
    #print(second_user_prefs[index])
    #if first_user_prefs.index


# In[124]:

#Print the first review
#print(reviews[0])
#print("\n",reviews[1])
#print("\n",reviews[10000])


# In[125]:

#from nltk.tokenize import sent_tokenize
#import json
#first_review = json.loads(reviews[0])
#second_review = json.loads(reviews[1])
#nth_review = json.loads(reviews[10000])


# In[126]:

#review_text = first_review['text']
#review_text2 = second_review['text']
#review_text3 = nth_review['text']


# In[127]:

# Sentiment Intensity Analyzer Using Vader
#from __future__ import print_function
#from nltk.sentiment.vader import SentimentIntensityAnalyzer
#from nltk import tokenize
#reviews = [first_review, second_review, nth_review]
#sid = SentimentIntensityAnalyzer()
#for review in reviews:
 #   review_text = review['text']
 #   rating = review['stars']
 #   ss = sid.polarity_scores(review_text)
 #   print(review_text + "\n\nActual rating: {}".format(rating))
  #  for k in sorted(ss):
   #     print("{0}:{1} ".format(k, ss[k]),end='')
    #print("\n\n")


# In[128]:




# In[ ]:




# In[ ]:



