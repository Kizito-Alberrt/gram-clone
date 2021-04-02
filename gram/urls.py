from django.urls import path 
from gram.views import index 

urlpatterns = [ 
    path('',index.as_view(), name = 'index')
]