
from django.conf import settings
from django.conf.urls import url
from words import views

urlpatterns = [

    url(r'^$', views.HomePage.as_view(), name='home'),

]
