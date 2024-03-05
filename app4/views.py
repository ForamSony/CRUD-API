from .models import Student
from .serializer import studentserializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from .custompermission import  MyPermission
from .customAuth import CustomAuthentication
class StudentModelViewSet(viewsets.ModelViewSet):

     queryset = Student.objects.all()
     serializer_class = studentserializer
    # authentication_classes = [BasicAuthentication]
 #   authentication_classes = [SessionAuthentication]
     #authentication_classes = [TokenAuthentication]
     authentication_classes = [CustomAuthentication]
     permission_classes = [IsAuthenticated]
    # permission_classes = [IsAdminUser]
    #permission_classes = [AllowAny]
    #permission_classes = [IsAuthenticatedOrReadOnly]
    #permission_classes=[DjangoModelPermissions]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
#    permission_classes = [MyPermission]


