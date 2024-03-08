from .models import Student
from .serializer import studentserializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, \
    DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from .custompermission import MyPermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle,ScopedRateThrottle
from app4.throttling import JackRateThrottle
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView


# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = studentserializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     # throttle_classes = [AnonRateThrottle, UserRateThrottle]
#     throttle_classes = [AnonRateThrottle, JackRateThrottle]



class StudentList(ListAPIView):
  queryset = Student.objects.all()
  serializer_class = studentserializer
  throttle_classes = [ScopedRateThrottle]
  throttle_scope = 'viewstu'

class StudentCreate(CreateAPIView):
  queryset = Student.objects.all()
  serializer_class = studentserializer
  throttle_classes = [ScopedRateThrottle]
  throttle_scope = 'modifystu'

class StudentRetrieve(RetrieveAPIView):
  queryset = Student.objects.all()
  serializer_class = studentserializer
  throttle_classes = [ScopedRateThrottle]
  throttle_scope = 'viewstu'

class StudentUpdate(UpdateAPIView):
  queryset = Student.objects.all()
  serializer_class = studentserializer
  throttle_classes = [ScopedRateThrottle]
  throttle_scope = 'modifystu'

class StudentDestroy(DestroyAPIView):
  queryset = Student.objects.all()
  serializer_class = studentserializer
  throttle_classes = [ScopedRateThrottle]
  throttle_scope = 'modifystu'