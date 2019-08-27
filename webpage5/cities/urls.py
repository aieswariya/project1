from django.urls import path

from .views import homepage, searchresult

urlpatterns = [
    path('', homepage.as_view(), name='homepage'),
    path('search', searchresult.as_view(), name='search_result'),
    
]