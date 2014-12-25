from django.conf.urls import url
from listings import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^frontend/$', views.frontend, name='frontend$'),

    url(r'^category/(?P<category>\w+)/$', views.view_category, name='view_category'),

    url(r'^myposts/view/$', views.my_posts, name='my_post'),
    url(r'^myposts/edit/(?P<post_id>\d*)/$', views.edit_post, name='edit_post'),
    url(r'^myposts/delete/(?P<post_id>\d*)/$', views.delete_post, name='delete_post'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^signout/$', views.signout, name='signout'),
    ]