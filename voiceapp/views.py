from django.shortcuts import render
from models import *

# Create your views here.
def index(request):
	context={}
	if request.method == "GET":
		if 'input' in request.GET and request.GET['input']!='':
			words = request.GET['input'].split()
			result = []
			for w in words:
				try:
					a = Keyword.objects.get(keyword__icontains=w)
					a = a.content_set.all()
					for i in a:
						result.append(i)
				except Keyword.DoesNotExist:
					pass
			context['result'] = result
			if len(result) == 0:
				context['none'] = 'None'
			context['input'] = request.GET['input']
	return render(request, 'voiceapp/index.html',context)