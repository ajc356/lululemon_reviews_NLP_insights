# Actionable Insights from Lululemon Reviews

Amanda Cheney  
Metis Project 4  
November 13, 2020    

**Motivation**  

Lululemon customers are known for writing detailed product reviews aimed at giving the company feedback as well as helping other potential customers inform their purchases. However, there are two major impediments to deriving actionable insights from these reviews, first the majority of the data is unstructured (since it's mostly just text) and second, numeric ratings are unable to convey specific information.  

**Objective** 

Efficiently deriving actionable insights from all online reviews of all 13 of lululemon's best-selling sports bras using natural language processing and unsupervised learning.

**Data Sources** 

9,000+ unique reviews of all 13 of lululemon's best-selling sports bras scraped from lululemon.com using Selenium.

**Methods**

Spacy for text preprocessing and lemmatization. Feature extraction with TFIDF and CV. Topic Modeling with LSA, LDA and NMF.   

Final model uses TFIDF and NMF and selects 6 core topics using  scree, cumulative variation explained and t-SNE plots to validate optimal number of topics.  

**Key Findings**

6 core topics across all product reviews. 

1. expectations vs experience  
2. size/fit  
3. support  
4. style/design   
5. comfort  
6. performance  

Positive reviews have an equal distribution across all topics while negative reviews are overwhelmingly concerned with product performance, size/fit as well as how the customer’s experience with the product compares with their expectations. 

Analysis has value added for product design team as well as customer experience - as demonstrated in Streamlit app - [Lululemon Review Curator] (https://share.streamlit.io/ajc356/lululemon_reviews_nlp_insights/main/review_curator.py ). 

**Technologies Used**

- Gensim
- SpaCy
- t-SNE
- Jupyter Notebook
- Python
- Pandas
- Scikit-learn
- Matplotlib
- Selenium
- Streamlit 


**Skills Demonstrated** 

- Natural Language Processing
- Unsupervised Learning
- Dimensionality Reduction
- Topic Modeling
- Visualization
- Web scraping 





