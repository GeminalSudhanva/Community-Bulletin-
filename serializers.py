from rest_framework import serializers
from .models import User, Post, Category, Attachment, Report

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'age', 'role']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    user = UserSerializer()
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'category', 'user', 'created_at', 'updated_at']

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'post', 'file_path', 'file_type']

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'post', 'user', 'reason', 'created_at']
