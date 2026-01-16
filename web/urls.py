from django.urls import path
from . import views

#pour  faire posts.page ou posts.all-posts pour le name de l'url
app_name = "posts"

urlpatterns = [
    path("" , views.posts_list ,  name="all-posts"),
    path("<slug:slug>" , views.post_page , name="page")
]