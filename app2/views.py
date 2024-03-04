from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from .models import Student
from .serializer import studentserializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

#function base apiview
# @api_view()
# def hello_world(request):
#     return Response({'msg': 'hello world'})

# @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg': 'hello world'})

# @api_view(['POST'])
# def hello_world(request):
#     if request.method == 'POST':
#       print(request.data)
#       return Response({'msg': 'hello POST METHOD'})

# @api_view(['GET','POST'])
# def hello_world(request):
#     if request.method == 'GET':
#       print(request.data)
#       return Response({'msg': 'hello GET METHOD'})
#
#     if request.method == 'POST':
#       print(request.data)
#       return Response({'msg': 'hello POST METHOD','data':request.data})

#function base apiview
@api_view(['GET','POST','PUT','PATCH','DELETE']) # Bydefault inside this is GET
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_api(request,pk=None):

    if request.method == 'GET':
        # id = request.data.get('id')
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = studentserializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = studentserializer(stu, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'This is POST Request'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUESTcd)

    if request.method == 'PUT':
        # id = request.data.get('id')
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = studentserializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': ' complate data updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    if request.method == 'PATCH':
        # id = request.data.get('id')
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = studentserializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partially updated'})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        # id = request.data.get('id')
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'data deleted'})

#classbase apiview
# class studentAPI(APIView):
#     def get(self,request,pk=None,formate=None):
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = studentserializer(stu)
#             return Response(serializer.data)
#         stu = Student.objects.all()
#         serializer = studentserializer(stu, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, formate=None):
#         serializer = studentserializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'This is POST Request'},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUESTcd)
#
#     def put(self, request, pk=None, formate=None):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = studentserializer(stu,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': ' complate data updated'})
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     def patch(self, request, pk=None, formate=None):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = studentserializer(stu,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Partially updated'})
#         return Response(serializer.errors)
#
#     def delete(self, request, pk=None, formate=None):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg': 'data deleted'})


#generic api views and mixins

#list and create which is nit required pk
# class Studentlc(GenericAPIView,ListModelMixin,CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = studentserializer
#
#     def get(self,request,*args,**kwargs): #list
#         return self.list(request,*args,**kwargs)
#
#     def post(self,request,*args,**kwargs):#create
#         return self.create(request,*args,**kwargs)
#
#
# #update,retreive,destroy which requires pk
# class Studenturd(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = studentserializer
#
#     def put(self,request,*args,**kwargs): #update
#         return self.update(request,*args,**kwargs)
#
#     def get(self,request,*args,**kwargs): #retrieve
#         return self.retrieve(request,*args,**kwargs)
#
#     def delete(self,request,*args,**kwargs): #destroy
#         return self.destroy(request,*args,**kwargs)


#
#
# class StudentList(ListAPIView):
#   queryset = Student.objects.all()
#   serializer_class = studentserializer
#
# class StudentCreate(CreateAPIView):
#   queryset = Student.objects.all()
#   serializer_class = studentserializer
#
# class StudentRetrieve(RetrieveAPIView):
#   queryset = Student.objects.all()
#   serializer_class = studentserializer
#
# class StudentUpdate(UpdateAPIView):
#   queryset = Student.objects.all()
#   serializer_class = studentserializer
#
# class StudentDestroy(DestroyAPIView):
#   queryset = Student.objects.all()
#   serializer_class = studentserializer
#
# class StudentListCreate(ListCreateAPIView):
#   queryset = Student.objects.all()
#   serializer_class = studentserializer
#
# class StudentRetrieveUpdate(RetrieveUpdateAPIView):
#   queryset = Student.objects.all()
#   serializer_class = studentserializer
#
# class StudentRetrieveDestroy(RetrieveDestroyAPIView):
#   queryset = Student.objects.all()
#   serializer_class = studentserializer
#
# class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
#   queryset = Student.objects.all()
#   serializer_class = studentserializer