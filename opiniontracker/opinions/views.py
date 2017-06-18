from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ask_for_query(request):
	return render(request, 'ask_for_query.html')
def return_opinions(request, query):
	return HttpResponse(query)