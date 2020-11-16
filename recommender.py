import pandas as pd 
import numpy as np 
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
import heapq


# @st.cache
def Review_Recommender(final_df, product, num=1, exp=1, size=1, support=1, 
    style=1, comfort=1, performance=1):
    """
    Takes in a product name, number of reviews to be displayed and weights for each 
    topic to return the selected number of reviews based on the relative importance 
    the user has assigned to each topic.
    """

    only_prod = final_df[final_df['product_name']==product] # mask final_df to
    # limit to product specified by user
    
    small_prod = only_prod[['product_name','Topic_0', 'Topic_1', 'Topic_2', 
    'Topic_3', 'Topic_4','Topic_5']] #remove extraneous columns for calculating
    # cosine similarity below 

    average_review  = small_prod.mean() # find average review by taking the finding
    # the mean of the small_prod DF

    # apply topic weights to transform average review into user specific review
    average_review = average_review.multiply([exp, size, support, style, comfort, performance])
    user_vector = average_review.values.reshape(1,-1) 
    
    #compare the user_vector to each review in the small_prod dataframe calculating
    # their level of similarity with cosine_similarity and storing values in list
    similarity_matrix = []
    similarity_matrix = cosine_similarity(small_prod.iloc[:,1:], user_vector)
        
    # use similarity scores to find the top k reviews most similar to the user 
    # vector and then identify the indexes for those k reviews which can then be 
    # applied to the only_prod DF to access the review content which was not 
    # included in the small_prod DF
    indx = heapq.nlargest(num, range(len(similarity_matrix)), similarity_matrix.take)

    co = []
    pr = []
    for i in indx: 
        co.append(only_prod.iloc[i]['content'])
        pr.append(only_prod.iloc[i]['product_name'])
    return co,pr 

