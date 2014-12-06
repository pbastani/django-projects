from django.conf.urls import url

from timeline import views

# using generic views
urlpatterns = [
    url(r'^$', views.index, name='index'),
]