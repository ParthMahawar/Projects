from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	htm = '''
			<html>
			<head>
			webpage
			</head>
			<body>
			<form name = 'test'>
			<input type = 'text' name = 'encryption'>
			<a href "/encryption"
			<input type = 'submit' name = 'Submit'>
			</a href>
			</body>
			</html>
		  '''
	return HttpResponse(htm)