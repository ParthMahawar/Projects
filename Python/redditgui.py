import praw
from tkinter import *
from urllib.request import urlopen
import time

root = Tk()

def fixup(string, n):
	for ind in range(0, len(string), n):
		string = string[:ind] + '	' + string[ind:]
	return string

def get_comments():
	
	try:
		postRead = postlist[int(box2.get()) - 1]
	except:
		postRead = postlist[0]

	box2.destroy()
	submit2.destroy()
	output.destroy()

	print(type(postRead.comments))
	comms = postRead.comments
	comms.replace_more()

	output2 = Text(root, wrap = WORD)
	output2.grid(row = 0, column = 1)#, fill = Y)

	for i in comms:
		textstr = ''
		try:
			if i.is_root:
				textstr += i.body
				textstr += '\n------\n'
				for reply in i.replies:
					#textstr += fixup(reply.body, 73)
					textstr += '>>>>>' + reply.body
					textstr += '\n------'
					textstr += '\n\n'
				
				textstr += '------------------'
				textstr += '\n\n'
			output2.insert(END, textstr)
		except Exception as e: print(e)

	def BACK():
		back.destroy()
		scroller.destroy()
		output2.destroy()
		ask_subreddit()

	scroller = Scrollbar(root)
	scroller.grid(row = 0, column = 2, sticky = 'ns')#, fill = Y)
	scroller.config(command = output2.yview)
	output2.config(yscrollcommand = scroller.set)
	back = Button(command = BACK, text = 'Back')
	back.grid(row = 1, columnspan = 3)

def get_subreddit():
	global postlist
	global output
	global box2
	global submit2

	try:
		sub = reddit.subreddit(box.get())
	except Exception as e:
		print(e)
		sub = reddit.subreddit('all')

	submit.destroy()
	box.destroy()

	posts = sub.hot(limit = 10)
	postlist = []
	titlelist = []

	for post, num in zip(posts, range(1, 11)):
		postlist.append(post)
		titlelist.append(str(num)+'. '+post.title)

	titlestr = ''

	for title in titlelist:
		titlestr += title
		titlestr += '\n'

	output = Text(root, wrap = WORD)
	output.pack()
	output.insert(END, titlestr)

	box2 = Entry(root, width = 24)
	submit2 = Button(root, width = 20, command = get_comments, text = 'Submit')
	box2.pack()
	submit2.pack()

	def upvote(postno):
		postlist[int(postno)-1].upvote()

	if logged_in:
		up = Button(root, width = 20, command = lambda:(upvote(box2.get())), text = 'Upvote')
		up.pack()

def ask_subreddit():
	global box
	global submit
	Begin.destroy()
	box = Entry(root, width = 24)
	box.pack()
	submit = Button(root, width = 20, text = 'Submit', command = get_subreddit)
	submit.pack()

def authenticate(user = None, pword = None):
	global reddit
	print(user)
	print(pword)
	
	if logged_in:
		reddit = praw.Reddit(client_id = '6O2l6qiy-aVOuA',
			client_secret = None,
			user_agent = 'reddit is very fun by u/bots-',
			redirect_uri = 'http://example.com',
			username = user,
			password = pword)

	else:
		reddit = praw.Reddit(client_id = '6O2l6qiy-aVOuA',
			client_secret = None,
			user_agent = 'reddit is very fun by u/bots-',
			redirect_uri = 'http://example.com')

	#reddit.read_only = True
	urlopen(reddit.auth.url(['identity'], '...', implicit=True))
	print(reddit.auth.url(['identity'], '...', implicit=True))
	time.sleep(15)
	implicit()
	ask_subreddit()

def login():
	global logged_in
	#global ASDF
	#global FDSA

	#ASDF = None
	#FDSA = None
	logged_in = True

	Begin.destroy()
	Log.destroy()

	def remove():
		usertxt.destroy()
		passtxt.destroy()
		ASDF = user.get()
		FDSA = pw.get()
		user.destroy()
		pw.destroy()
		ewlbf.destroy()
		authenticate(user = ASDF, pword = FDSA)

	usertxt = Label(root, text = 'User:')
	passtxt = Label(root, text = 'Pass:')
	user = Entry(root)
	pw = Entry(root)

	ewlbf = Button(text = 'submit', command = remove)

	usertxt.grid(row = 0, column = 0)
	passtxt.grid(row = 1, column = 0)
	user.grid(row = 0, column = 1)
	pw.grid(row = 1, column  = 1)
	ewlbf.grid(row = 2, column = 1)

Begin = Button(root, text = 'Guest', command = authenticate)
Begin.pack()
Log = Button(root, text = 'Login', command = login)
Log.pack()

mainloop()