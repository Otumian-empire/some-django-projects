from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employees
from .serializers import employeesSerializer


class employeeList(APIView):
    def get(self, request):
        empList = employees.objects.all()
        myserializer = employeesSerializer(empList, many=True)
        return Response(myserializer.data)

    def post(self, request):
        if request.method == 'POST':

            return Response({
                'request': request
            })
        else:
            self.get(request)
