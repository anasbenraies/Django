from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('register/' , views.register, name='register'),
    path('about/' , views.about, name='about'),
    path('contact/' , views.contact, name='contact'),
    path('login/',views.login_view , name='login'),
    path("logout/",views.logout_view , name="logout"),

]
