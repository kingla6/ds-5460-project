
import pandas as pd
import os
import re

#import multiprocessing as mp
#pool = mp.Pool(mp.cpu_count())


# reviews = pd.DataFrame(columns=['marketplace', 'customer_id', 'review_id', 'product_id',
#        'product_parent', 'product_title', 'product_category', 'star_rating',
#        'helpful_votes', 'total_votes', 'vine', 'verified_purchase',
#        'review_headline', 'review_body', 'review_date', 'category'])
# for file in os.listdir('archive-5'):
#     category = re.search('amazon_reviews_us_(.+?)_v1|amazon_reviews_(.+?)_US_v1', file).group(1)
#     print(category)
#     df = pd.read_csv("./archive-5/amazon_reviews_us_Wireless_v1_00.tsv", sep='\t', error_bad_lines=False)
    
#     reviews = reviews.append(df)

reviews = pd.DataFrame(columns=['marketplace', 'customer_id', 'review_id', 'product_id',
       'product_parent', 'product_title', 'product_category', 'star_rating',
       'helpful_votes', 'total_votes', 'vine', 'verified_purchase',
       'review_headline', 'review_body', 'review_date', 'category'])
file = "amazon_reviews_us_Wireless_v1_00.tsv"
category = re.search('amazon_reviews_us_(.+?)_v1|amazon_reviews_(.+?)_US_v1', file).group(1)
df = pd.read_csv("./archive-5/amazon_reviews_us_Wireless_v1_00.tsv", sep='\t', error_bad_lines=False)
df['category'] = category
reviews = reviews.append(df)


print(reviews.columns)
print(reviews.shape)