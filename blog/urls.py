from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('pl', views.pl, name='pl'),
    path('tx', views.tx, name='tx'),
    path('phan', views.phan, name='phan'),
    path('progress', views.progress, name='progress'),
    path('contact', views.contact, name='contact'),
    # path('')
]
