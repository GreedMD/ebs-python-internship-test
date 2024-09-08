from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.blog.views import BlogItemView, BlogListView, CategoryViewSet, CreateBlogView, CreateCommentView

router = DefaultRouter(trailing_slash=False)
router.register(
    r"blog/categories",
    CategoryViewSet,
    basename="category",
)

urlpatterns = [
    path("blog", BlogListView.as_view(), name="blog_list"),
    path("blog/<int:pk>", BlogItemView.as_view(), name="blog_item"),
    path("blog/create", CreateBlogView.as_view(), name="create_blog"),
    path("blog/<int:pk>/comment", CreateCommentView.as_view(), name="create_comment"),
    *router.urls,
]
