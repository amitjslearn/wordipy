#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 22:11:38 2019

@author: amit
"""
import re
from word2number import w2n
import vocabulary as voc
from nltk.stem import PorterStemmer, WordNetLemmatizer

#global output

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
    input_str_list = input_str.split(" ")
    
    intersection = set(process_words) & set(voc.tuple_.keys())
    
    #print(intersection)
    if len(intersection):
        '''
        if double, triple (tuples) is present in the input
        '''
        times = intersection.pop()
        times_num = int(voc.tuple_[times])
        item = input_str.replace(times, '')[len(times):] + sep
        output = (item*times_num).strip() # lstrip() can also be used, but strip trims spaces from both sides
        last_char_remove = True if sep != ""  else False
        if last_char_remove:
            output = output[:-1]
        check = final_abbreviationize(output, input_str_list)
        if check:
            return check
        return output
    else:
        return final_abbreviationize(input_str, input_str_list)

def final_abbreviationize(output, input_str_list):            
    if all([x.isupper() for x in input_str_list]) or all(x.isupper() for x in output.split()): 
        '''
        if all are upper ex: C M -> CM
        '''
        pattern = re.compile(r's+') 
        output = re.sub(pattern, '', output)
        #assert(len("".join(input_str_list)) == len(a))
        output = output.replace(" ", "")
    return output

abbr= abbreviationize('Triple BAM', sep= ",")
print(abbr, "len: ", len(abbr))

# abbr2 = abbreviationize("C M")
# print(abbr2)
# print(amountize('two dollars'))
