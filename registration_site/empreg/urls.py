from django.urls import path


from . import views
urlpatterns=[
       path('',views.home,name='home'),
       path('result/',views.display,name='display'),
       path('search/',views.search,name='search'),
       path('searchnew/',views.searchnew,name='searchnew')
       
       ]
       