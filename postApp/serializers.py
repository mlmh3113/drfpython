from rest_framework import serializers
from .models import Post , Category
from django_filters import rest_framework as filters

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PostFilter(filters.FilterSet):
    category = filters.NumberFilter(field_name='category', lookup_expr='exact')
    name = filters.CharFilter(method='filter_by_search',lookup_expr='icontains')

    def filter_by_search(self, queryset, value):
        return queryset.filter(title__icontains = value)

    class Meta:
        model = Post
        fields = {
            'category' : ['exact'],
            'title': ['icontains'],
        }


class PostSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source = "category.name")
    
    class Meta:
        model = Post
        fields = ('id','title','sub_title','content','image','created_at','category','category_name')
        filter_class = PostFilter        