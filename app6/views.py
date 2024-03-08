from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


    # filter_backends = [DjangoFilterBackend]
    # #filterset_fields = ['city']
    # filterset_fields = ['name','city']


    filter_backends = [SearchFilter]
    search_fields = ['city']
    # search_fields = ['name', 'city']
    # search_fields = ['^name'] # start with
    #search_fields = ['=name'] # exact match
    # search_fields = ['@name'] # full text search
    # search_fields = ['$name'] # regex search
    # def get_queryset(self):
    #     user = self.request.user
    #     return Student.objects.filter(passby=user)
