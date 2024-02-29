from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views

router = DefaultRouter()
router.register('stud', views.StudentViewSet, basename="stud")

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),

    path('stuinfo/<int:pk>',views.student_list),
    path('stuinfo/',views.student_details),
    path('studentapp/',views.Studentapp.as_view()),
]
