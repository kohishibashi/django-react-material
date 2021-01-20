from rest_framework import serializers
from .models import Post

# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ['id', 'title', 'body']

class PostSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)


class PostListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=50)
    body = serializers.CharField(max_length=4000)

class AccountSerializer(serializers.Serializer):
    name = serializers.CharField()
    mail = serializers.EmailField()

class CommentListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    body = serializers.CharField(max_length=255)
    # account = AccountSerializer()
    account_name = serializers.ReadOnlyField(source='account.name', read_only=True)
    account_mail = serializers.ReadOnlyField(source='account.mail', read_only=True)
