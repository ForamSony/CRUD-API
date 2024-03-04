from django.urls import path,include
from app4 import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stdapi',views.StudentModelViewSet,basename='student')

urlpatterns = [
   path('', include(router.urls)),
   path('auth/',include('rest_framework.urls', namespace='rest_framework'))

]

