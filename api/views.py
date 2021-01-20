# from django.shortcuts import render
# from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import PostSerializer, PostListSerializer, CommentListSerializer

# from django.http import HttpResponse
from .models import Post

 
# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class PostViewSet(APIView):
    serializer_class = PostSerializer

    def get(self, request, format=None):
        return Response({'message': 'テストAPIです'})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            messeage = f'メッセージ： {name}'
            return Response({'message': messeage})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request, pk=None):
        return Response({'message': 'PUTメソッド使ってます'})

    def patch(self, request, pk=None):
        return Response({'message': 'PATCHメソッド使ってます'})

    def delete(self, request, pk=None):
        return Response({'message': 'DELETEメソッド使ってます'})

class PostListView(APIView):

    def get(self, request, format=None):
        posts = Post.objects.all()
        # res_posts = [
        #     {'id': post.id, 'title': post.title, 'body': post.body}
        #     for post in posts
        # ]
        res_post = PostListSerializer(posts, many=True)
        print(res_post.data)
        return Response(res_post.data)

class PostDetailView(APIView):
    
    def get(self, request, pk=None, format=None):
        post = Post.objects.get(id=pk)
        comments = post.comment_set.all()
        res_comment = CommentListSerializer(comments, many=True)
        # print(res_comment.data)

        # res_post = {
        #     'id': post.id,
        #     'title': post.title,
        #     'body': post.body,
        # }
        res_post = PostListSerializer(post)
        print(dict(res_post.data, **{'comment': res_comment.data}))

        return Response(dict(res_post.data, **{'comment': res_comment.data}))