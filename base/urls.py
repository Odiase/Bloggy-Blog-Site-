from django.urls import path
from .views import contact, home,sign_up,Login,Logout

urlpatterns = [
    path("",home,name = "home"),
    path("sign-up/",sign_up,name = "sign-up"),
    path("login/",Login,name ="login"),
    path("logout/",Logout,name = "logout"),
    path("contact/",contact,name = "contact"),
]