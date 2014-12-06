from django.conf.urls import url
from portfolio import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^users/(?P<username>\w+)/profile/$', views.user_profile, name='user_profile'),
    url(r'^friends/find/$', views.find_friends, name='find_friends'),
    url(r'^portfolio/delete/$', views.delete_portfolio, name='delete_portfolio'),
    url(r'^photos/delete/(?P<position>\d+)/$', views.delete_photo, name='delete_photo'),
    url(r'^photos/edit/(?P<position>-?\d)/$', views.edit_photo, name='edit_photo'),
    url(r'^photos/upload/$', views.upload_photos, name='upload_photos'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.signin, name='login'),
    url(r'^logout/$', views.signout, name='logout'),
    ]