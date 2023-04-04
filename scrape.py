import snscrape.modules.twitter as sntwitter
import pandas as pd
from textblob import TextBlob




def extract_tweets(num_of_tweets, country_code):
    tweets_list = []
    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i , tweet in enumerate(sntwitter.TwitterSearchScraper('Election near:"{}" since:2023-02-25 until:2023-03-01'.format(country_code)).get_items()):
        if i > num_of_tweets:
            break
        analysis = TextBlob(tweet.content)
        polarity = analysis.sentiment.polarity
        subjectivity = analysis.sentiment.subjectivity
        tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username, polarity, subjectivity])


    # Creating a dataframe from the tweets list above
    tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username', 'Polarity', 'Subjectivity'])
    return tweets_df
