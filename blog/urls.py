from django.urls import path
from blog.views import (
    CategoryListAPIView,
    BlogListAPIView,
    BlogRetriveAPIView,
    BlogCreateAPIView,
    BlogDestroyAPIView,
)

# urls
urlpatterns = [
    path("categories/", CategoryListAPIView.as_view(), name="list_category"),
    path("list/", BlogListAPIView.as_view(), name="list_blog"),
    path("list/<pk>/", BlogRetriveAPIView.as_view()),
    path("list/<pk>/remove/", BlogDestroyAPIView.as_view()),
    path("", BlogCreateAPIView.as_view()),
]