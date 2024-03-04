from django.urls import path,include
from app4 import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from app4.auth import customauthtoken


router = DefaultRouter()
router.register('stdapi',views.StudentModelViewSet,basename='student')

urlpatterns = [
   path('', include(router.urls)),
   path('auth/',include('rest_framework.urls', namespace='rest_framework')),
   # path('gettoken/', obtain_auth_token),
   path('gettoken/', customauthtoken.as_view()),
]

