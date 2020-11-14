import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import re 


# remove numbers and punctuation
def make_alphabetic(text):
    """
    A helper function to remove numbers and punctuation before passing the
    data to my preprocessing pipeline
    """
    text = re.sub(r'[^A-Za-z\s]', '', text)
    return text.lower()


nlp = spacy.load('en_core_web_sm', disable=['tagger', 'parser', 'ner'], n_process=-1)

custom_stopwords = ['bra', ' bra', 'bra ', 'bras', 'sport', 'sports'
    'a','aa', 'ab', 'b','c','cb','bc','d','dc','cd','dd','ddd', 
    'dddd', 'e', 'ee', 'f', 'ff', 'g', 'gg', 'h', 'hh', 'l', 'm', 'n', 'o', 'p',
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'x', 's', 'm', 'xs', 'l', 'xl',
    'xxl', 'lbs' , 'lb', '', ' ', '  ', '\n', '-PRON-', '\ufeff1'
    ]

stopwords_list=STOP_WORDS.union(custom_stopwords)

def lemmatize_pipe(doc):
    lemma_list = [str(tok.lemma_) for tok in doc
                 if tok.is_alpha and tok.text and tok.lemma_ not in stopwords_list]
    lem_string = " ".join(lemma_list)
    return lem_string.lower()

def preprocess_pipe(texts, batch_size=100):
    preproc_pipe = []
    for doc in nlp.pipe(texts, batch_size=batch_size, n_threads=-1):
        preproc_pipe.append(lemmatize_pipe(doc))
    return preproc_pipe