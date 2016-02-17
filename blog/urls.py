from django.conf.urls import patterns, url
from blog import views, json_views

urlpatterns = patterns(
	                'blog.json_views',
                    url(r'^blog_collection/$', 'blog_collection'),
                    url(r'^single_blog/(?P<id>[0-9]+)$', 'detailed_blog'),
	                # url(r'^$',views.index,name='index'),
	              
	                 #url(r'^(?P<blog_id>\d+)/$',views.blog,name='blog'),

	                )