from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^travels/$', views.TravelList.as_view()),
    url(r'^travels/(?P<pk>[0-9]+)/$', views.TravelDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

