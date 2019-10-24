import vocabulary as voc
from nltk.stem import PorterStemmer, WordNetLemmatizer

input_str = input("Enter the amount: ").lower()

words = input_str.split(" ")

porter_stemmer=PorterStemmer()
stemmed_words=[porter_stemmer.stem(word) for word in words]

#nltk.download('wordnet')

# init lemmatizer
lemmatizer = WordNetLemmatizer()

currency = words[-1] if words[-1] in voc.currencies.keys() else ""
amount = words[:-1]
print(stemmed_words)
output_str = ""

#remove dollars dollar use nltk or ther library 
