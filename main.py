#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 22:11:38 2019

@author: amitjslearn
"""
import re
from word2number import w2n
import vocabulary as voc
from nltk.stem import PorterStemmer, WordNetLemmatizer
input_str = 'two thousand dollars'
'''
uncomment the below line
'''
#input_str = input("Enter the amount: ").lower()

words = input_str.split(" ")

porter_stemmer=PorterStemmer()
stemmed_words=[porter_stemmer.stem(word) for word in words]

#nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
lemmatized_words=[lemmatizer.lemmatize(word=word, pos='n') for word in words]
currency = stemmed_words[-1] if stemmed_words[-1] in voc.currencies.keys() else "" #raise exception /try except
#currency_symbol = voc.currencies[currency]
amount = " ".join(words[:-1])
w2n.word_to_num(amount)
amount_num = w2n.word_to_num(amount)
print(amount_num)
print(stemmed_words, currency)
#print(lemmatized_words, amount)
currency_symbol = voc.currencies[currency]
print(currency_symbol)
output_str = currency_symbol + str(amount_num)
print(output_str)

def abbreviations(ip):
    pass
