from __future__ import print_function
import json
import csv
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

sid = SentimentIntensityAnalyzer()

with open ("yelp_dataset_challenge_round9/yelp_academic_dataset_review.json") as f, open("yelpreviews.csv","wb") as reviewscsv:

    # Since the json files are newline delimited
    review_count = 0
    for line in f:
        review_json = json.loads(line)

        user_id = review_json['user_id']
        business_id = review_json['business_id']
        text = review_json['text']
        rating = sid.polarity_scores(text)['compound']

        review_count += 1
        print("review ",review_count)
        csvwriter = csv.writer(reviewscsv, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow([user_id, business_id, rating])
