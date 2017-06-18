import tweepy
import jsonpickle

CKEY = 'zdPkoIyHXDwqP1yJ7PqnBfWWo'
CSCRT = 'd1jt2lCDpYlnGHLVIVIrW3VO0No13CBX8L0AbCioEAPtq8vNNQ'
auth = tweepy.OAuthHandler(CKEY, CSCRT)

try:
	redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
	print "'Error: Can't obtain request token."

ATKN = '827929258685243393-wfGungow47XfVxx8FFbe6r5ADYcwITB'
ASCRT = '2jwSs2ghnQQTbRaueOXU0uqNDFJE9M3P2wqjnIoLcbYBY'

api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):

	def on_status(self, status):
		print(status.text)
	def on_connect(self):
		print('connect')
	def on_error(self, status_code):
		print('error')
		print(status_code)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['python'])