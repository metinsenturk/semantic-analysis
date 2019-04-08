import pandas as pd
from features.text_preprocessing import SpaCyProcessing, NLTKProcessing

# init library
cleanup = SpaCyProcessing()


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


def apply_text_processing(revs_list, to_file=None, read_from_file=False, remove_stopwords=True, remove_alpha=True, remove_punct=True, remove_pos=True, lemmatize=True, remove_short_words=True):
    
    df_series = revs_list

    if read_from_file is False:
        df_dump = df_series.apply(lambda x: [tuple(i) for i in cleanup.doc_sent_clean_up(x)])
        if to_file is not None:
            df_dump.to_csv(f'../data/processed/{to_file}', index=False)
    else:
        df_dump = pd.read_csv(f'../data/processed/{to_file}')

    return df_dump
