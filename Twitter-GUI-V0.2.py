import tweepy
import jsonpickle
from Tkinter import *
from wordcloud import WordCloud
import matplotlib.pyplot as plot

root = Tk()
root.geometry('1200x600')

def searchtwitter(query, tweetcount):

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
	#print '--------------------------------------------------------------'
	#print counter, 'Tweets Found'
	#print '--------------------------------------------------------------'

	wordlist = []

	for tweet in tweetlist:
		words = tweet.split()
		for word in words:
			wordlist.append(word)

	cloudstr = ''

	for word in wordlist:
		if word != '''"text":''':
			cloudstr += word + ' '

	cloudstr.strip()

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
	finallist = []
	finalstr =''


	for tweet in tweetlist:
		finallist.append(tweet[9:])

	finallist.append('-------------------------------------------------------------------------')
	finallist.append(str(counter) + ' Tweets Found')
	finallist.append('-------------------------------------------------------------------------')

	for score in scores:
		for key, val in wordscores.iteritems():
			if val == score:
				iterlst.append(key)
		finallist.append(str(iterlst) + ' - ' + str(score))
		iterlst = []

	for thing in finallist:
		finalstr += thing + '\n'

	endlst = [finalstr, cloudstr]

	return endlst
def cloudgen():
	cloud = WordCloud().generate(var[1])
	plot.figure()
	plot.imshow(cloud)
	plot.axis('off')
	plot.show()
def thirdstep():
	global var
	global output
	global scroller
	global cloudbutton
	var = searchtwitter(text, num)
	output = Text(root, height = 100, width = 147, wrap = WORD)
	output.pack(side = LEFT, fill = Y)
	scroller = Scrollbar(root)
	scroller.pack(side = RIGHT, fill = Y)
	cloudbutton = Button(root, width = 147, command = cloudgen)
	cloudbutton.pack(side = LEFT)
	scroller.config(command = output.yview)
	output.config(yscrollcommand = scroller.set)
	output.insert(END, var[0])

def addcount():
	global num
	num = box.get()
	label.destroy()
	box.destroy()
	sub.destroy()
	thirdstep()

def nextstep():
	global box
	global label
	global sub

	label = Label(root, text = 'Number of tweets to search')
	label.pack()
	box = Entry(root, width = 20)
	sub = Button(root, width = 20, text = 'Submit', command = addcount)
	box.pack()
	sub.pack()

def addquery():
	global text
	text = box.get()
	print text
	box.destroy()
	sub.destroy()
	nextstep()

box = Entry(root, width = 24)
sub = Button(root, width = 20, text = 'Submit Query', command = addquery)
box.pack()
sub.pack()
root.mainloop()