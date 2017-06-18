import tweepy
import jsonpickle as js
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plot

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
tweets = int(input('How Many Tweets: '))
counter = 0

tweetlist = []

for status in tweepy.Cursor(api.search, q=query).items(tweets):
	tweetlist.append(js.encode(status, unpicklable = True))

iterlst = []
tweettextlist = []
allwords = ''

for tweet in tweetlist:
	objects = tweet.split(',')
	for thing in objects:
		thing = thing.strip()
		if thing.startswith('"text"') or thing.startswith('"name"'): tweettextlist.append(thing)
		#tweettextlist.append(thing)

namelist = []

for text in tweettextlist:
	if text.startswith('"text"'):
		namelist = []
		if '\n' in text:
			text.replace('\n', '''
				''')
		elif '\\' in text:
			continue
		elif text.endswith('}]') or text.endswith('}'):
			continue
		if text not in iterlst:
			counter += 1
			iterlst.append(text)
			print(counter, ':', text, '\n')
			allwords += text[9:]
	else:
		if query.lower() in text.lower() and text.lower() not in namelist:
			print(text)

print(counter, 'tweets found')

cloud = WordCloud(height = 1440, width = 2560).generate(allwords)
plot.figure()
plot.imshow(cloud)
plot.axis('off')
plot.show()