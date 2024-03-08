from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


    # filter_backends = [DjangoFilterBackend]
    # #filterset_fields = ['city']
    # filterset_fields = ['name','city']

#search filter==========
    # filter_backends = [SearchFilter]
    # search_fields = ['city']
    # search_fields = ['name', 'city']
    # search_fields = ['^name'] # start with
    #search_fields = ['=name'] # exact match
    # search_fields = ['@name'] # full text search
    # search_fields = ['$name'] # regex search

#ordering filter===========
    filter_backends = [OrderingFilter]
    # ordering_fields =['name']
    ordering_fields =['name','city']

    # def get_queryset(self):
    #     user = self.request.user
    #     return Student.objects.filter(passby=user)
