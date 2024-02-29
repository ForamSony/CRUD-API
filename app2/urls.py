from django.urls import path
from app2 import views

urlpatterns = [
   # path('studentapp2/', views.hello_world),
   #  path('studentapi/', views.student_api),
   #  path('studentapi/<int:pk>/', views.student_api),
   #  path('stdapi/', views.studentAPI.as_view()),
   #  path('stdapi/<int:pk>/', views.studentAPI.as_view()),
   #    path('stdapi/', views.StudentList.as_view()),
   # path('stdapi/', views.StudentCreate.as_view()),
  # path('stdapi/<int:pk>/', views.StudentRetreive.as_view()),
# path('stdapi/<int:pk>/', views.StudentUpdate.as_view()),
#path('stdapi/<int:pk>/', views.StudentDestroy.as_view()),
#path('studentlc/', views.Studentlc.as_view()),
#path('studenturd/<int:pk>/', views.Studenturd.as_view()),

    path('stuapi/',views.StudentList.as_view()),
    path('stuapi/',views.StudentCreate.as_view()),
    path('stuapi/<int:pk>/',views.StudentRetrieve.as_view()),
    path('stuapi/<int:pk>/',views.StudentUpdate.as_view()),
    path('stuapi/<int:pk>/',views.StudentDestroy.as_view()),
    path('stuapi/<int:pk>/',views.StudentListCreate.as_view()),
    path('stuapi/<int:pk>/',views.StudentRetrieveUpdate.as_view()),
    path('stuapi/<int:pk>/',views.StudentRetrieveDestroy.as_view()),
    path('stuapi/<int:pk>/',views.StudentRetrieveUpdateDestroy.as_view()),
]

