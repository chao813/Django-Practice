from django.shortcuts import render
from .models import Post
#from django.http import HttpResponse

# Create your views here.
posts = [
	{
		'author': 'YuanChao',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'August 27, 2018'
	},
	{
		'author': 'Alex Goneh',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'August 28, 2018'
	}
]

def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})

def login(request):
	return render(request, 'blog/login.html')

