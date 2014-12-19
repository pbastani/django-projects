from django.conf.urls import url
from listings import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    ]