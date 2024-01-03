from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Student
from .serializers import StudentSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# Create your views here.

class StudentsApiView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
  
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)
    

class StudentDataView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)
    



# class StudentApiView(APIView):

#     def get(self, request, pk=None, format=None):

#         if pk is not None:
#             student = Student.objects.get(id=pk)
#             serializer = StudentSerializer(student)
#             return Response(serializer.data)
#         else:
#             Response({'message':'Student Data not found'})
        
#         student = Student.objects.all()
#         serializer = StudentSerializer(student, many=True)
#         return Response(serializer.data)


#     def post(self, request, format=None):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message':'Student Data Created'}, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#     def put(self, request, pk, format=None):
#         student = Student.objects.get(id=pk)
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message':'Complete Student Data Updated'}, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#     def patch(self, request, pk, format=None):
#         student = Student.objects.get(id=pk)
#         serializer = StudentSerializer(student, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message':'Partial Student Data Updated'}, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#     def delete(self, request, pk, format=None):
#         student = Student.objects.get(id=pk)
#         student.delete()
#         return Response({'message':'Student Data deleted'}, status=status.HTTP_202_ACCEPTED)
