#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import nltk
import string
import random


# In[6]:


from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# In[7]:


#Reading Text Corpses
f = open('C:/Users/ASUS/OneDrive/Desktop/Chatbot/chatbot.txt.','r', errors='ignore')
raw_doc = f.read()
raw_doc = raw_doc.lower() # Converting entire text to Lowercase
nltk.download('punkt') # Using the Punkt tokenizer
nltk.download('wordnet') # Using the wordnet dictionary
nltk.download('omw-1.4')


# In[8]:


sentence_tokens = nltk.sent_tokenize(raw_doc) 
word_tokens = nltk.word_tokenize (raw_doc)


# In[9]:


# Performing text pre-processing

lemmatizer = WordNetLemmatizer()

remove_punc_dict = dict((ord (punct), None) for punct in string.punctuation)


# In[10]:


def LemTokens (tokens):
    return [lemmatizer.lemmatize(token) for token in tokens]


# In[11]:


def LemNormalize(text):
    return LemTokens (nltk.word_tokenize(text.lower().translate (remove_punc_dict)))


# In[12]:


#Define Greeting Functions
greet_inputs = ('hello','hi','wasssup','how are you?')
greet_responses = ('hi','hey','hey, there!','there, there!')


# In[13]:


def greet(sentence):
    for word in sentence.split():
        if word.lower() in greet_inputs:
            return random.choice(greet_responses)


# In[14]:


def response(user_response):
    robo1_response = ''
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sentence_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        robo1_response = robo1_response + "I am sorry! I don't understand you"
        return robo1_response
    else:
        robo1_response = robo1_response + sentence_tokens[idx]
        return robo1_response


# In[17]:


#Defining Chat Flow
flag = True
print("Hello! My name is AIBot. Start typing your text after greeting to talk to me. If you want to exit, type Bye!")

while flag:
    user_response = input()
    user_response = user_response.lower()
    if user_response != 'bye':
        if user_response =='thanks' or user_response == 'thank you':
            print('Bot: Your are welcome..')
        else:
            if greet(user_response) is not None:
                print('Bot:' + greet(user_response))
            else:
                sentence_tokens.append(user_response)
                word_tokens = word_tokens + nltk.word_tokenize(user_response)
                final_words = list(set(word_tokens))
                print('Bot:', end='')
                print(response(user_response))
                sentence_tokens.remove(user_response)
    else:
        flag = False
        print('Bot: Bye! Take care...')


# In[ ]:





# In[ ]:




