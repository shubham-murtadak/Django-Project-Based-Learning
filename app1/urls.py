
from django.urls import path
from . import views
urlpatterns = [
    path('index/',views.index,name="index"),#use when urls created in project
    path('greet2',views.greet2,name="in")
]
