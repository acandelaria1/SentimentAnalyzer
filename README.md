# SentimentAnalyzer

This is a submission for the Yelp dataset challenge Round 9. The goal of this project is to take
the yelp data set and train a sentiment Analysis classifier to rate reviews based on purely text.
We can use a clustering technique with 5 centroids each representing 1-5 star ratings. It is possible that 
validation of the classifier will be done against actual ratings associated with each review.

### Considerations for the sentiment analysis classifier 
- remove all stop words using nltk library
- investigate data wrangling capabilities using pandas and possibly pyspark for parralelism
- use an unsupervised technique to cluster reviews based on sentiment scores
- possibly consider TF IDF to identify most relevant and useful words for identifying what a user values in restaurants 

## Building the restaurant recommender system
- Build a user-tem collaborative filtering recommender system that takes sentiment analysis from each customer and then finds
 similar customers with similar sentiment for the same restaruant.
- Utilize the jaccardian distance between several customer vectors to determine similarity
- Utilize the utility matrix to offer recommendations

### Things that I do not yet understand
- how to handle a dataset as large as the Yelp Dataset
    - Can handle this on local machine. Considered and explored aws ec2 spot instance but successfully ran operations on local machine 
      and will continue with this until cloud resources become necessary.
- What kind of data preprocessing should be done
    - Tokenizing sentences from reviews, tokenizing words from sentences, removing stop words.
    - Have sample code to remove stop words but instead using vader to found compound polarity
- what kind of visualizations should be made to effectively demonstrate findings
- Do official yelp star ratings actually mean anything or is there bias in these making validation of the classifier against them questionable
- Could binary vectors be used to to find similarity between customers? Giving all ratings below 3 a rating of 0 and 1 for every rating 3 and above
- if binary vector are used for user profiles then a jaccardian distance can be used to determine similarity
- if ratings values of 1-5 are used then using the cosine distance will be better suited for comparing the user profiles
- how will we present final product?

Profiling results for uploading json file into pandas data frame, time measured in seconds
![alt text](https://raw.githubusercontent.com/acandelaria1/SentimentAnalyzer/master/profile.png)

An illustration of the utilization of string indexer to turn Yelp user and business Ids into integers
![alt_text](https://raw.githubusercontent.com/acandelaria1/SentimentAnalyzer/master/stringindexer.png)
