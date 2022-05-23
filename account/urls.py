from django.urls import path
from .views import profile_page, all_profile_blogs, create_profile, update_profile, subscribe

urlpatterns = [
    path("create/",create_profile, name = "create-profile"),
    path("update/",update_profile, name = "update-profile"),
    path("<str:id>/",profile_page,name = "account"),
    path("<str:id>/subscribe/", subscribe, name = "subscribe"),
    path("<str:id>/blogs/", all_profile_blogs,name = "profile-blogs")
]