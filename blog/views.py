
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from blog.serializers import CategoryListSerializer,BlogSerializer
from django.utils.text import slugify
from rest_framework_simplejwt.authentication import JWTAuthentication


class CategoryListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CategoryListSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()


class BlogListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = BlogSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()


class BlogRetriveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = BlogSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()


class BlogCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = BlogSerializer
    

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data["title"]
        slug = slugify(title)
        author = self.request.user
        serializer.save(author=author, slug=slug)
        return serializer


class BlogDestroyAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = BlogSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()