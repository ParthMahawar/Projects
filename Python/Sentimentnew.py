import requests
import json
import ast
import tweepy
import jsonpickle as js

file = open('debug.txt', 'w')
file.truncate()

CKEY = '8l9rpQ2EgpXFS0T8nkOljzZvM'
CSCRT = '5cEPzHrUsAhVseWQCnpoQsuPXzmUfQDN67NFISB63SGCuBYS6m'
auth = tweepy.OAuthHandler(CKEY, CSCRT)

try:
	redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
	print("'Error: Can't obtain request token.")

ATKN = '827929258685243393-D2Hg4UPQaGHPHnmfOvNn55qxF25AhVN'
ASCRT = 'fMD5e3GLH3KLaBWftMr9ZvtQnwKLb7neHN8ksmYdAV0DE'

auth.set_access_token(ATKN, ASCRT)

api = tweepy.API(auth)

query = input('Enter Search: ')
numTweets = int(input('How Many Tweets: '))
counter = 0

tweets = []

for status in tweepy.Cursor(api.search, q=query).items(numTweets):
	if len(tweets) < numTweets:
		tweets.append(js.encode(status, unpicklable = True))

tweetlist = []

#print(tweets)
#print('''
#	-------------------------------------------------------------------
#	''')
for tweet in tweets:
	txt = js.encode(tweets, unpicklable = False)
	#print(txt)
	split = txt.split(',')

	for i in split:
		i = i.strip()

		if '}' in i:
			i.replace('}', '')

		if i.startswith('\\"text\\"') and i[9:] not in tweetlist and i[:-1] not in tweetlist:
			counter += 1
			
			if i.endswith('''"'''):
				i = i [:-1]
			
			print(counter, ':', i[9:])
			tweetlist.append(i[9:])

#print(tweetlist)

dic = {'data': []}

for i in range(len(tweetlist)):
	tweet = tweetlist[i]
	file.write('\nTweet ' + str(i) + ': ' + tweet)
	if '\\' in tweet:
		modTweet = tweet.replace('\\', '')
		file.write('\n(rep) Tweet ' + str(i) + ': ' + modTweet)
	dic['data'].append({'text': modTweet, 'query':query})

url = 'http://www.sentiment140.com/api/bulkClassifyJson'

r = requests.post(url, data = json.dumps(dic))

polarities = json.loads(r.text)
#print(polarities)

final = []

for dat in polarities['data']:
	final.append(dat['polarity'])
	#print(dat['text'])

#print(final)

print(sum(final)/len(final))

final2 = []
for i in final:
	if i != 2:
		final2.append(i)

print(final2)
try:
	print(sum(final2)/len(final2)/(4/100))
except ZeroDivisionError:
	print('Somehow everything is neutral.')
print('Positive:', final2.count(4))
print('Negative:', final2.count(0))
