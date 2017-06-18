import praw
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plot
import pytumblr

CommID = raw_input('Enter the Post ID: ')
allwords = ''
comment_counter = 0

reddit = praw.Reddit(client_id = '-fFb3PKTm0KmTA',
	client_secret = 'yBdSvEPn7xPz-zgR5eE8LxOgOs8',
	user_agent = 'Encryptor/Python/PRAW v0.0.1 by u/bots-',
	username = 'bots-',
	password = '!@#$%^&*()')

tumblrClient = pytumblr.TumblrRestClient(
  'XwbtExPv52sZiQKGc2PN8mDnitwEFmUpcjUN95SHu4muuzGjko',
  'g6l4E95W0LhH6MXLtEYzHpk4FwuCYTivI5gTYsiAzzh34UfpIB',
  'Hd7lMrl3AhS2ikZtmAYs5Fbr1kI0CM0mB6xKhhHCmr08ELi8Ok',
  'v1bUGCF78IKKpPIdvyTq1EzEO0EKGQQlrdo8bdUSWubYDuUQzV'
)

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

print(comment_counter)
cloud = WordCloud(height = 4320, width = 7680).generate(allwords)
plot.figure()
plot.imshow(cloud)
plot.axis('off')
plot.savefig('wordcloud.png', format = 'png',bbox_inches = 'tight', dpi = 600)
tumblrClient.create_photo('imgurnoupload', state = 'published', link = 'http://reddit.com/'+CommID, data = 'wordcloud.png', caption = topPost.title)
topPost.reply('Wordcloud for all the comments at\nhttps://imgurnoupload.tumblr.com\n\nIf you\'re downvoting, please specify what the problem is in the comments.\n\nThe Image is on Tumblr as Imgur blocks uploads from India.')
plot.show()