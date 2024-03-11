from django.contrib import admin
from django.urls import path, include
from app9 import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('stdapi', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('',include(router.urls)),

]
