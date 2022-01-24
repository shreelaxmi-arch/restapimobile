from django.urls import path
from .api import MobileCreateApi,MobileApi,MobileUpdateApi,MobileDeleteApi
urlpatterns=[
   
    path('/api/create',MobileCreateApi.as_view()),
     path('/api',MobileApi.as_view()),
    path('/api/update/<int:pk>',MobileUpdateApi.as_view()),
    path('/api/delete/<int:pk>',MobileDeleteApi.as_view()),
]