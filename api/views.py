from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.decorators import api_view
from .serializers import EmployeeSerializer
from .models import Employee
import json


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/Employees-list/',
        'Detail View' : '/employee-detail/<int:id>/',
        'Add' : '/employee-add/',
        'Delete' : '/employee-delete/<int:id>',
        'Update' : '/employee-update/'
    }
    
    return Response(api_urls)
    
@api_view(['GET'])
def ShowEmployeesList(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees,many = True)
    return Response(serializer.data)
    
@api_view(['GET'])
def ShowEmployee(request,pk):
    employees = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(employees,many = False)
    return Response(serializer.data)
    
    
@api_view(['POST'])
def addEmployee(request):
    serializer = EmployeeSerializer(data = request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({'status' : HTTP_200_OK,'msg' : 'Employee Added SuccessFully'})
    else:
        return Response({'status' : HTTP_400_BAD_REQUEST,'msg' : 'Error'})
        
@api_view(['POST'])
def updateEmployee(request):
    pk = request.data['id']
    employee = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(instance = employee, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status' : HTTP_200_OK,'msg' : 'Employee Updated SuccessFully'})
    else:
        return Response({'status' : HTTP_400_BAD_REQUEST,'msg' : 'Error'})
        
        
@api_view(['GET'])
def deleteEmployee(request,pk):
    employee = Employee.objects.get(id=pk)
    employee.delete()
    return Response({'status' : HTTP_200_OK,'msg' : 'Employee Deleted SuccessFully'})
    
        
        
        
        

    