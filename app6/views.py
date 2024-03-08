from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentSerializer
from .mypagination import Mycursor
# from .mypagination import Mylimit
#from .mypagination import My
# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #pagination_class = My
    # pagination_class = Mylimit
    pagination_class = Mycursor


