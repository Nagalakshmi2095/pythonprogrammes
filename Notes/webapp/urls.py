from django.contrib import admin
from django.urls import path
from webapp import views

urlpatterns=[
    path('',views.Noteview.as_view()),
    path('<int:pk>/',views.Notedetailview.as_view()),

]

