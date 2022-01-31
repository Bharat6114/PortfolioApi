from rest_framework import serializers
from blog.models import Category,Blogs


class CategoryListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = "id","title"


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    category = CategoryListSerializer(read_only=True, many=True)
    category_ids = serializers.PrimaryKeyRelatedField(
        write_only =True,many=True, queryset=Category.objects.all(),source="category"
    )
    class Meta:
        model=Blogs
        fields = "id","blog_title","blog_image","blog_description","category","created_at","updated_at"
