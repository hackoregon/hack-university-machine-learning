
# coding: utf-8

# In[12]:

from porter import stem as port
from lovins import stem as lov
sentence = 'Is there anything harder than finding roots with a stemmer of trees in bunches of'
sentence += ' ugly duckling geese, goslings, goose, chicken, swimming swan words?'

def stem_all(text, stemmer=port):
    return ' '.join(stemmer(w) for w in text.split())

stem_all(sentence)


# In[13]:

stem_all(sentence, stemmer=lov)

