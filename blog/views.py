from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from blog.models import Blog



# View for home page
def index(request):
	latest_blogs = Blog.objects.all().order_by('pub_time')
	single_latest_blog = Blog.objects.all().order_by('?')[0]
	related_blogs = Blog.objects.order_by("-pub_time")[:4]
	t = loader.get_template('index.html')
	context_dict = {'latest_blogs':latest_blogs,'single_latest_blog':single_latest_blog,'related_blogs':related_blogs,}
	c = Context(context_dict)
	return HttpResponse(t.render(c))

# View for blog description page
def blog(request, blog_id):
	single_blog = get_object_or_404(Blog, pk=blog_id)
	related_blogs = Blog.objects.order_by("-pub_time")[:4]
	t = loader.get_template('blog.html')
	c = Context({'single_blog':single_blog,'related_blogs':related_blogs,})
	return HttpResponse(t.render(c))
    












