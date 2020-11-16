import streamlit as st
import pandas as pd
import pickle
from recommender import Review_Recommender
import heapq


st.markdown("""
<style>
body {
    background-color: #d7d2cb;
}
</style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #C60C30;'>Lululemon Review Curator</h1>", unsafe_allow_html=True)

st.write('''
### Reading reviews is an integral part of the online shopping experience. 
Yet sifting through hundreds of reviews written by customers whose needs differ 
from yours is a time consuming process. Welcome to lululemon review curator 
which provides a curated collection of reviews specifically tailored 
to your product needs. 
''')

st.write(
'''
** To get started, please select one of lululemon's best-selling sports bras from the dropdown list below.**
'''
	)

product = st.selectbox('Product:', (
		'Like a Cloud Bra Light Support, B/C Cup',
       'Energy Bra Medium Support, B–D Cup',
       'Free To Be Bra Wild Light Support, A/B Cup',
       'Invigorate Bra Long Line Medium Support, B/C Cup',
       'Flow Y Bra Nulu Light Support, B/C Cup',
       'Ebb to Street Bra Light Support, C/D Cup',
       'Enlite Bra Zip Front High Support, A–E Cups',
       'Energy Bra Long Line Medium Support, B–D Cup',
       'Ebb To Street Bra Light Support, A/B Cup',
       'Run Times Bra High Support, B–E Cups',
       'Energy Bra High Neck Medium Support, B–D Cup',
       'Free To Be Serene Bra Long Line Light Support, C/D Cup Online Only',
       'Enlite Bra Weave High Support, A–E Cup Online Only'))

st.write(
'''
#### Compared to the average person, how important are the following topics for your product needs? \n
'''
	)

size = st.selectbox('Size/Fit :', (
	'1: about the same importance',
	'2: somewhat more important',
	'3: quite a bit more important',
	'4: a lot more important',
	'5: much more important'
	))

support = st.selectbox('Support', (
	'1: about the same importance',
	'2: somewhat more important',
	'3: quite a bit more important',
	'4: a lot more important',
	'5: much more important'
	))

style = st.selectbox('Style/Design', (
	'1: about the same importance',
	'2: somewhat more important',
	'3: quite a bit more important',
	'4: a lot more important',
	'5: much more important'
	))

comfort = st.selectbox('Comfort', (
	'1: about the same importance',
	'2: somewhat more important',
	'3: quite a bit more important',
	'4: a lot more important',
	'5: much more important'
	))

performance = st.selectbox('Overall Performance', (
	'1: about the same importance',
	'2: somewhat more important',
	'3: quite a bit more important',
	'4: a lot more important',
	'5: much more important'
	))


data = pd.read_csv('final_df.csv')

data= data[data['product_name']==product]

num = st.number_input('How many reviews would you like to view?', min_value=1, max_value=len(data))


content, prod = Review_Recommender(data, product=product, num=num,
	 # exp=int(exp[0]),  # decide not to include expectations vs experience as
	 # aspect of review curatior 
	 size=int(size[0]), 
	 support=int(support[0]), 
	 style=int(style[0]), 
	 comfort=int(comfort[0]), 
	 performance=int(performance[0]))

def diplay(my_input):
	long_string = " "
	for i in range(len(my_input)):
		long_string + '- ' + (my_input[i])
		# my_thing + '-'
	return long_string

st.write('''
#### Your curated reviews of:
	''')

st.write(f"{prod[-1]}")


output = diplay(content)

