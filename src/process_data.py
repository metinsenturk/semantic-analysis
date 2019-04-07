from features.text_preprocessing import SpaCyProcessing, NLTKProcessing

def textprocessing(test_reviews):
    p = NLTKProcessing(test_reviews)

    reviews1 = []
    for review in test_reviews:
        review = p.lower(review)
        review = p.punctuation(review)  # todo: bug
        review = p.stopwords(review)
        review = p.freqwords(review)
        review = p.shortwords(review)
        review = p.rarewords(review)
        # review = p.spelling(review)
        review = p.tokenize(review)
        review = p.stemming(review)
        review = p.lemnatize(review)
        reviews1.append(review)

    return(reviews1)

def text_processing(text, remove_stopwords=True, remove_alpha=True, remove_punct=True, remove_pos=True, lemmatize=True, remove_short_words=True):
    # init library
    cleanup = SpaCyProcessing()
    
    # return cleaned version
    return cleanup.doc_sent_clean_up(text)