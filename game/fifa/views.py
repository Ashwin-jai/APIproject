from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *
from rest_framework.response import Response

from.models import *
@api_view(['POST'])
def create_employee(request):
    if request.method == 'POST':
        newdata = EmployeeSerializers(data=request.data)
        if newdata.is_valid():
            newdata.save()
            return Response({"success":"datacreated"}, status=status.HTTP_201_CREATED)
        return Response({"error":"badrequest"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getrecords(request):
    if request.method=='GET':
        record=Employee.objects.all()
        result=EmployeeSerializers(record,many=True)
        return Response(result.data,status=status.HTTP_200_OK)
@api_view(['GET'])

def get_allrecord(request):
    if request.method=='GET':
        res=Employee.objects.all()
        record=EmployeeSerializers(res,many=True)
        return Response(record.data, status=status.HTTP_200_OK)


@api_view(['GET'])

def filter_record(request):
    if request.method=='GET':
        search=request.GET.get('searchrecord',None)
        record=Employee.objects.filter(name=search)
        result=EmployeeSerializers(record,many=True)
        return Response(result.data, status=status.HTTP_200_OK)

@api_view(['PUT'])

def update_record(request):
    if request.method=='PUT':
        new = request.GET.get('searchrecord', None)
        try:
            a=Employee.objects.get(name=new)
        except Exception as e:
            print(e)
        update=updateserialzers(a, data=request.data)
        print(update)
        if update.is_valid():
            update.save()
            print("ashwanth")
            return Response(update.data,status=status.HTTP_200_OK)

@api_view(["DELETE"])

def delete_record(request):
    record = Employee.objects.get(name ='arun')
    if record:
        record.delete()
        return Response({"ok": "Record Deleted"}, status= status.HTTP_200_OK)

# Create your views here.
