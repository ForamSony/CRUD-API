from django.urls import path
from app6 import views


urlpatterns = [

    path('stdapi/', views.StudentList.as_view()),
]
