from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.serializers import BlogSerializer
from blog.models import Blog

@api_view(['GET'])
def blog_collection(request):
    if request.method == 'GET':
        total_blogs = Blog.objects.all()
        serializer = BlogSerializer(total_blogs,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def detailed_blog(request, id):

    try:
        single_blog = Blog.objects.get(id=id)
    except StatusReport.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogSerializer(single_blog)
        return Response(serializer.data)
        							


