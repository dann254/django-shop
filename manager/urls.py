from django.conf.urls import url
from .views import addstock, sell, stock, item, Reports, Delete, Update

urlpatterns=[
    url(r'^addstock/', addstock,name='addstock'),
    url(r'^sell/', sell,name='sell'),
    url(r'^stock/', stock,name='stock'),
    url(r'^item/(?P<id>\d+)/$', item,name='item'),
    url(r'^delete/(?P<id>\d+)/$', Delete,name='delete'),
    url(r'^update/(?P<id>\d+)/$', Update,name='update'),
    url(r'^reports/', Reports,name='reports'),
]
