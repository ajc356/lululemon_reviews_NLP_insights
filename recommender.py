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
    'Topic_3', 'Topic_4','Topic_5']]

    average_review  = small_prod.mean()

    for i in average_review.index:
        if str(i) == 'Topic_0':
            weight = exp
        elif str(i) == 'Topic_1':
            weight = size
        elif str(i) == 'Topic_2':
            weight =  support
        elif str(i) == 'Topic_3':
            weight = style
        elif str(i) == 'Topic_4':
            weight = comfort
        elif str(i)== 'Topic_5':
            weight = performance
        else:
            weight = 1
    
        average_review[str(i)]  = average_review[str(i)]*weight
        user_vector = average_review.values.reshape(1,-1)
    
    #compare the average review --now manipulated with user weights to be the 
    # user vector, to the outlet vectors in the dataframe
    similarity_matrix = []
    #loop through each row in small_prod, computing the cosine similarity between
    # said row and the user vector(average_review)    
    for index, row in small_prod.iloc[: ,1: ].iterrows():
        outlet_vector = row.values.reshape(1,-1)
        #calculate cosine similarity
        similarity_score = cosine_similarity(user_vector, outlet_vector)
        #append each cosine simiilarity score onto our list
        similarity_matrix.append(similarity_score)
        
    #use similarity scores to find the top k reviews most similar to the user vector
    holder = np.array(similarity_matrix)
    indx = heapq.nlargest(num, range(len(holder)), holder.take)

    co = []
    pr = []

    for i in indx: 
        co.append(only_prod.iloc[i]['content'])
        pr.append(only_prod.iloc[i]['product_name'])
    return co,pr 

