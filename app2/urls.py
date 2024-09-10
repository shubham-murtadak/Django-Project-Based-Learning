
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index2,name="index"),#use when urls created in project
    path('np2/',views.np2,name="in"), #use leading / in path always else get error!
    path('np3/',views.next_page,name="next_page")
]
