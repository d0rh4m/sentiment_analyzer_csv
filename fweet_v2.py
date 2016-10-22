import tweepy 
from textblob import TextBlob

# Get consumer keys 
consumer_key = input("Consumer key: ")
consumer_secret = input("Consumer secret: ")

# Get access keys
access_token = input("Access token: ")
access_token_secret = input("Access_token_secret: ")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

queryTopic = input("What is it that you are looking for?: ")

print("Getting access to Twitter...")

public_tweets = api.search(queryTopic)

count = 0
for tweet in public_tweets: 
	count = count + 1	
	print("Here is tweet number", count)
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	if analysis.sentiment.polarity > 0:
		print("The tweet is positive")
	elif analysis.sentiment.polarity == 0:
		print("The tweet is neutral")
	else:
		print("The tweet is negative")	
	print ("")

# Option to download CSV 

decision = input("Would you like to download a csv file?: ")

while decision not in ("yes", "no"):
	decision = ("Please type either yes or no!: ")

count_csv = 0
if decision == "yes":
	print("CSV Downloaded!")
	with open('tweets.csv', "w", newline='') as csvfile:
		writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
		writer.writerow(("Count", "Tweets", "Sentiment"))
		for tweet in public_tweets:
			count_csv = count_csv + 1	
			tweetlist = tweet.text
			analysis = TextBlob(tweet.text)
			if analysis.sentiment.polarity > 0:
				tweet_sentiment = "POSITIVE"
			elif analysis.sentiment.polarity == 0:
				tweet_sentiment = "NEUTRAL"
			else:
				tweet_sentiment = "NEGATIVE"

			writer.writerow((count_csv, tweetlist, tweet_sentiment))
elif decision == "no":
	print("OK then")
