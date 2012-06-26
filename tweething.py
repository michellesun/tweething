import tweepy

gtweetslist = []
keytweets = []

def goodtweet(tweet):
	trigger = False
	for w in badwords:
		if w in tweet:
			trigger = True
			break
	if trigger == False:
		gtweetslist.append(tweet)

# search for AT LEAST ONE of keywords AND NO ONE of badwords
# for each keyword in keywords 
	# goodtweet = text of tweet containing keyword and not containing badwords
	# gtweetslist.append(goodtweet)
# print gtweetslist

keywords = ["worms", "tattoo", "vomit", "underwear", "ridiculous", "fail"]
badwords = ["sad", "#", "funeral","death","crash", "cancer", "nobody", "sick", "vagina", "cares"]

for keyword in keywords:
	searched = tweepy.api.search(keyword, "en")
	for tweet in searched:
		keytweets.append(tweet.text)
	for each in keytweets:
		goodtweet(each)

print '\n'.join(gtweetslist)