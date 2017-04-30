from __future__ import print_function
import json
import sqlite3

conn = sqlite3.connect('Yelp.db')
c = conn.cursor()

with open ("yelp_dataset_challenge_round9/yelp_academic_dataset_review.json") as f:

    # Since the json files are newline delimited
    review_count = 0
    for line in f:
        review_json = json.loads(line)

        review_id = review_json['review_id']
        user_id = review_json['user_id']
        business_id = review_json['business_id']
        stars = review_json['stars']
        date = review_json['date']
        text = review_json['text'].replace("'","''")
        useful = review_json['useful']
        funny = review_json['funny']
        cool =  review_json['cool']
        review_type =  review_json['type']

        args = (review_id, user_id, business_id, stars, date, text, useful, funny, cool, review_type)
        # Insert a review into the sqlite DB
        print("review {} added".format(review_count))
        sql_string = "INSERT INTO REVIEW VALUES ('{0}','{1}','{2}', {3},'{4}','{5}', {6}, {7}, {8},'{9}')".format(*args)
        c.execute(sql_string)
        review_count += 1
# commit the changes to the db
conn.commit()
# close connection to db
conn.close()
