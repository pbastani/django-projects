from django.conf.urls import url
from portfolio import views

urlpatterns = [
    url(r'^$', views.my_profile, name='home'),

    url(r'^users/(?P<username>\w+)/follow/', views.follow, name='follow'),
    url(r'^users/(?P<username>\w+)/profile/$', views.user_profile, name='user_profile'),
    url(r'^users/(?P<username>\w+)/followers/$', views.user_followers, name='user_followers'),
    url(r'^users/(?P<username>\w+)/photos/$', views.user_photos, name='user_photos'),
    url(r'^users/(?P<username>\w+)/photos/(?P<position>-?\d+)/$', views.user_photo, name='user_photo'),

    url(r'^portfolio/delete/$', views.delete_portfolio, name='delete_portfolio'),

    url(r'^photos/view/$', views.my_photos, name='my_photos'),
    url(r'^photos/delete/(?P<position>\d+)/$', views.delete_photo, name='delete_photo'),
    url(r'^photos/edit/(?P<position>-?\d)/$', views.edit_photo, name='edit_photo'),
    url(r'^photos/upload/$', views.upload_photos, name='upload_photos'),

    url(r'^profile/view/$', views.my_profile, name='my_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),

    url(r'^followers/view/$', views.my_connections, name='my_followers'),
    url(r'^users/browse/$', views.browse_users, name='browse_users'),

    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.signin, name='login'),
    url(r'^logout/$', views.signout, name='logout'),
    ]