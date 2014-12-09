from django.conf.urls import url
from portfolio import views

urlpatterns = [
    url(r'^$', views.view_profile, name='home'),

    url(r'^users/(?P<username>\w+)/follow/', views.follow, name='follow'),
    url(r'^users/(?P<username>\w+)/profile/$', views.user_profile, name='user_profile'),
    url(r'^users/(?P<username>\w+)/friends/$', views.user_friends, name='user_friends'),
    url(r'^users/(?P<username>\w+)/photos/$', views.user_photos, name='user_photos'),
    url(r'^users/(?P<username>\w+)/photos/(?P<position>-?\d+)/$', views.user_photo, name='user_photo'),

    url(r'^friends/find/$', views.find_friends, name='find_friends'),
    url(r'^portfolio/delete/$', views.delete_portfolio, name='delete_portfolio'),

    url(r'^photos/view/$', views.view_photos, name='view_photos'),
    url(r'^photos/delete/(?P<position>\d+)/$', views.delete_photo, name='delete_photo'),
    url(r'^photos/edit/(?P<position>-?\d)/$', views.edit_photo, name='edit_photo'),
    url(r'^photos/upload/$', views.upload_photos, name='upload_photos'),

    url(r'^profile/view/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),

    url(r'^friends/view/$', views.view_friends, name='view_friends'),

    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.signin, name='login'),
    url(r'^logout/$', views.signout, name='logout'),
    ]