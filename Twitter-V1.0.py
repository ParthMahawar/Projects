import tweepy
import jsonpickle
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plot

endstring = ''
query = raw_input('Search: ')
tweetcount = raw_input('Number of tweets to search (max 100): ')

counter = 0
CKEY = '8l9rpQ2EgpXFS0T8nkOljzZvM'
CSCRT = '5cEPzHrUsAhVseWQCnpoQsuPXzmUfQDN67NFISB63SGCuBYS6m'
auth = tweepy.OAuthHandler(CKEY, CSCRT)

try:
	redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
	print "'Error: Can't obtain request token."

ATKN = '827929258685243393-D2Hg4UPQaGHPHnmfOvNn55qxF25AhVN'
ASCRT = 'fMD5e3GLH3KLaBWftMr9ZvtQnwKLb7neHN8ksmYdAV0DE'

api = tweepy.API(auth)

tweets = api.search(query, count = tweetcount)
tweetlist = []

txt = jsonpickle.encode(tweets, unpicklable = False)
#print txt
split = txt.split(',')

for i in split:
	i = i.strip()

	if '}' in i:
		x = list(i)
		del x[i.index('}')]
		i = str(x)

	if i.startswith('''"text"''') and '\\' not in i and i not in tweetlist and i[:-1] not in tweetlist:
		counter += 1
		
		if i.endswith('''"'''):
			i = i [:-1]
		
		print counter, ':', i[9:]
		tweetlist.append(i)

#print tweetlist
#print len(tweets)
print '--------------------------------------------------------------'
print counter, 'Tweets Found'
print '--------------------------------------------------------------'

wordlist = []

for tweet in tweetlist:
	words = tweet.split()
	for word in words:
		wordlist.append(word)

for word in wordlist:
	if word != '''"text":''':
		endstring += word + ' '

endstring.strip()
#cloud = WordCloud(font_path = 'C:\\Windows\\Fonts\\micross.ttf').generate(endstring)
cloud = WordCloud().generate(endstring)

#print wordlist
#print len(tweets)
#print counter
#print len(tweetlist)

wordscores = {}

for word in wordlist:
	word = word.upper()
	if word != '''"TEXT":''':
		if word in wordscores:
			wordscores[word] += 1
		else:
			wordscores[word] = 1

#print wordscores
#print len(wordlist)

scores = []

for key,val in wordscores.iteritems():
	scores.append(val)

scores.sort()
scores.reverse()
iterlst = []

for score in scores:
	if score not in iterlst:
		iterlst.append(score)
	else:
		pass
scores = iterlst[:]
iterlst = []

for score in scores:
	for key, val in wordscores.iteritems():
		if val == score:
			iterlst.append(key)
	print iterlst, '-', score
	iterlst = []

plot.figure()
plot.imshow(cloud)
plot.axis('off')
plot.show()