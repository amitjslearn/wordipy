try:
    import nltk
    from nltk.stem import WordNetLemmatizer  # ,PorterStemmer
except ImportError:
    print("Install nltk")


def processing(io):
    """
    this function helps in preprocessing
    """
    input_str = io
    input_lower = input_str.lower()

    words = input_lower.split(" ")

    #porter_stemmer=PorterStemmer()
    #stemmed_words=[porter_stemmer.stem(word) for word in words]

    #nltk.download('wordnet')

    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word=word, pos='n') for word in words]

    process_words = lemmatized_words
    return process_words
