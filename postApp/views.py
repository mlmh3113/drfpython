from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all()
        category = self.request.query_params.get('category', None)
        title = self.request.query_params.get('title', None)
        if category is not None :
            queryset = queryset.filter(category=category)
            return queryset
        elif title is not None:
            queryset = queryset.filter(title__icontains=title)
            return queryset
        else:
            return queryset


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer






