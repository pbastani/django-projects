from django.conf.urls import url
from listings import views

urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^signout/$', views.signout, name='signout'),
    ]