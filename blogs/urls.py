from django.urls import path
from .views import search_blogs, single_blog, create_blog, update_blog, delete_blog

urlpatterns = [
    path("create/", create_blog, name = "create-blog"),
    path("search/",search_blogs,name = "search-blog"),
    path("<str:id>/update/",update_blog,name = "update-blog"),
    path("<str:id>/delete/",delete_blog,name = "delete-blog"),
    path("<slug:slug>/<str:id>/", single_blog, name = "single-blog"),
]