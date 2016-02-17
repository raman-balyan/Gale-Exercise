from rest_framework import serializers
from blog.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'author', 'pub_time','category','limited_content','full_content','main_image','optional_image')
        
