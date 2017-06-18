import praw

reddit = praw.Reddit(client_id = '6O2l6qiy-aVOuA',
	client_secret = None,
	user_agent = 'reddit is very fun by u/bots-',
	redirect_uri = 'http://example.com')

reddit.read_only = True

sub = reddit.subreddit('all')
print('What subreddit would you like to visit?')
inp = input()

if inp.strip() != '':
	sub = reddit.subreddit(inp)

posts = sub.hot(limit = 10)

postlist = []

for post, num in zip(posts, range(1,11)):
	print(str(num)+'. '+post.title)
	postlist.append(post)

print("Which one's comments would you like to read?")
commNum = int(input()) - 1

postRead = postlist[commNum]

print('--------------')
comms = postRead.comments
comms.replace_more()

errcount = 0

for i in comms:
	try:
		if i.is_root:
			print(i.body)

			for reply in i.replies:
				print('>>>>>'+reply.body)
				print('--')
				print('\n')
			
			print('------------------')
			print('\n\n')
	except Exception as e: errcount += 1

print(errcount)