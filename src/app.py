# standard imports
import logging
import argparse
import itertools

# third party imports
import pandas as pd
import numpy as np

# local imports
import utilities
from model_data import run_topic_models, run_sentiment_models

# logging init
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(name)-25s - %(levelname)-8s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        logging.FileHandler('../data/logs/logs_app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("app")
logger.info("app started")

# init main
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--starti",
        type=int,
        default=0,
        help="start index of the competitors data."
    )
    parser.add_argument(
        "--endi",
        type=int,
        default=1,
        help="end index of the competitors data."
    )

    flags, unparsed = parser.parse_known_args()

    if input("Press any key to start..") is not None:
        # get_competitor_reviews(flags.starti, flags.endi)
        
        # read data
        df = pd.read_csv('../data/processed/hi_rws_0001_0256_complete.csv')
        logger.info("file is read.")
        
        n = 100
        
        df = utilities.fix_token_columns(df.copy().loc[:n,:])
        logger.info("file fix is completed.")
                
        run_topic_models(
            tokens_list=df.norm_tokens_doc[:n], 
            to_file='hi_rws_0001_0256_topics.csv', 
            transformations=False, 
            find_optimal_num_topics=False, 
            training=False,
            lsi=True,
            lda=True,            
            mallet=False,
            hdp=False
        )

        run_sentiment_models(
            revs_list=df.norm_tokens_doc.apply(lambda x: ' '.join(itertools.chain(*x)))[:n],
            sentiment_list=df.sentiment[:n],
            to_file='hi_rws_0001_0256_sentiments.csv',
            sgd=True,
            log=True,
            mnb=True,
            rdg=True
        )