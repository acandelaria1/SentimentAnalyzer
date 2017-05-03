from __future__ import print_function
import json
import csv

with open ("yelp_dataset_challenge_round9/yelp_academic_dataset_business.json") as f, open("yelpbusinesses.csv","w",encoding='utf-8') as businesscsv:

    # Since the json files are newline delimited
    for line in f:
        review_json = json.loads(line)

        business_id = review_json['business_id']
        name = review_json['name']
        try:
            csvwriter = csv.writer(businesscsv, delimiter=' ',quoting=csv.QUOTE_MINIMAL)
            csvwriter.writerow([business_id, name])
        except:
            print(business_id, name)
