from django.urls import path
from specific.views import *

app_name='hybrid'
urlpatterns=[
    path('specific1/',specific1,name='specific1'),
    path('specific2/',specific2,name='specific2'),
]