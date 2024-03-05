from django.urls import path,include
from app4 import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from app4.auth import customauthtoken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()
router.register('stdapi',views.StudentModelViewSet,basename='student')

urlpatterns = [
   path('', include(router.urls)),
   path('auth/',include('rest_framework.urls', namespace='rest_framework')),
   # path('gettoken/', obtain_auth_token),
   #path('gettoken/', customauthtoken.as_view()),
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),
]
