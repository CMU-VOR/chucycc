from django.shortcuts import render
from models import *

# Create your views here.
def index(request):
	context={}
	if request.method == "GET":
		if 'input' in request.GET and request.GET['input']!='':
			try:
				result = Keyword.objects.get(keyword__iexact=request.GET['input'])
				result = result.content_set.all()
				context['result'] = result
			except Keyword.DoesNotExist:
				context['none'] = 'None'
			context['input'] = request.GET['input']
	return render(request, 'voiceapp/index.html',context)