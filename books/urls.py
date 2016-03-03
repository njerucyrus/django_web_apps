from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^save/', views.saveBook, name='saveBook'),
    url(r'^books', views.getSavedBooks, name='getSavedBooks'),
    url(r'^issue/$', views.issueBook, name='issueBook'),
    url(r'^issued/$', views.getBooksIssued, name='getBooksIssued'),
    url(r'^books/$', views.getSavedBooks, name='getSavedBooks'),
    url(r'^$', views.home, name='home'),
    url(r'^home/', views.home, name='home'),

]