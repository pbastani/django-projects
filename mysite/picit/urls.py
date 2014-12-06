from django.conf.urls import url

from picit import views

# using generic views
urlpatterns = [
    url(r'^$', views.index, name='index'),
]