#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 22:11:38 2019

@author: amit
"""
#import funcs as fn
import re
from word2number import w2n
import vocabulary as voc
from nltk.stem import PorterStemmer, WordNetLemmatizer

def processing(io):
    
    input_str = io 
    input_lower = input_str.lower()

    words = input_lower.split(" ")
    
    #porter_stemmer=PorterStemmer()
    #stemmed_words=[porter_stemmer.stem(word) for word in words]
    
    #nltk.download('wordnet')
    
    lemmatizer = WordNetLemmatizer()
    lemmatized_words=[lemmatizer.lemmatize(word=word, pos='n') for word in words]
    
    process_words = lemmatized_words
    return process_words


def amountize(io):
    process_words = processing(io)
    if len(set(process_words) & set(voc.currencies.keys())):
        currency = set(process_words) & set(voc.currencies.keys()) #raise exception /try except
        currency_symbol = voc.currencies[currency.pop()]
        amount = " ".join(process_words[:-1])
        amount_num = w2n.word_to_num(amount)
        #print(amount_num)
       # print("intersection" , set(process_words) & set(voc.currencies.keys()))
        #print(process_words, currency)
        #print(process_words, amount)
        #currency_symbol = voc.currencies[currency]
        #print(currency_symbol)
        output_str = currency_symbol + str(amount_num)
        #print(output_str)
        return output_str

def abbreviationize(input_str, sep=""):
    """
    Gets and prints the spreadsheet's header columns

    Parameters
    ----------
    input_str : str
        The file location of the spreadsheet
    print_cols : bool, optional
        A flag used to print the columns to the console (default is
        False)

    Returns
    -------
    str
        a list of strings used that are the header columns
    """
    process_words = processing(input_str)
    #print(process_words)
    #print("hi", "lemm", lemmatized_words, "stem", stemmed_words)
    input_str_list = input_str.split(" ")
    
    #print(set(process_words), set(voc.tuple_.keys()))
    intersection = set(process_words) & set(voc.tuple_.keys())
    
    #print('ran before')
    print(intersection)
    if len(intersection):
        #print(intersection)
        times = int(voc.tuple_[intersection.pop()])
        item = input_str_list[1:]
        output = item*times
        print(sep.join(output))
        
        return output
        # if input is abbrevation type
        #print("intersection" , set(process_words) & set(voc.tuple_.keys()))
        
    
    if all([x.isupper() for x in input_str_list]): 
        '''if all are upper ex: C M -> CM
        '''
        pattern = re.compile(r's+') 
        a = re.sub(pattern, '', input_str)
        #print(input_str_list, a)
        assert(len("".join(input_str_list)) == len(a))
        #print(a)
        return a

print(abbreviationize("double All is well"))
print(amountize('two dollars'), sep=",")
