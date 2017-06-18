import praw
import matplotlib.pyplot as plt

CommID = input('Enter the Post ID: ')
allwords = ''
comment_counter = 0

reddit = praw.Reddit(client_id = '-fFb3PKTm0KmTA',
	client_secret = 'yBdSvEPn7xPz-zgR5eE8LxOgOs8',
	user_agent = 'Encryptor/Python/PRAW v0.0.1 by u/bots-',
	username = 'bots-',
	password = '!@#$%^&*()')

#tumblrClient = pytumblr.TumblrRestClient(
##  'XwbtExPv52sZiQKGc2PN8mDnitwEFmUpcjUN95SHu4muuzGjko',
##  'Hd7lMrl3AhS2ikZtmAYs5Fbr1kI0CM0mB6xKhhHCmr08ELi8Ok',
## # 'v1bUGCF78IKKpPIdvyTq1EzEO0EKGQQlrdo8bdUSWubYDuUQzV'
#)###

topPost = reddit.submission(id=CommID)
topPost.comments.replace_more()

print('\n')
print(topPost.title)
print('\n----\n')

postComments = topPost.comments.list()

for comment in postComments:
	try:
		print(comment.body)
		print('-------')
		for word in comment.body.split():
			allwords += word + ' '
		comment_counter += 1
	except:
		pass

wordscores = {}
wordlist = []

for word in allwords.lower().split():
	wordlist.append(word)

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
scorewords = {}

for key,val in wordscores.items():
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
	for key, val in wordscores.items():
		if val == score:
			iterlst.append(key)
	print(iterlst, '-', score)
	scorewords[score] = iterlst
	iterlst = []

print(wordscores)

print(1000*'-')

for key, val in scorewords.items():
	scorewords[key] = len(scorewords[key])

print(scorewords)

plt.hist(list(scorewords.values()),list(scorewords.keys()))
plt.show()