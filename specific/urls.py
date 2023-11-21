from django.urls import path
from specific.views import *
app_name='something'
urlpatterns=[
    path('yuvaraj/',yuvaraj,name='yuvaraj'),
    path('gv/',gv,name='gv'),

]