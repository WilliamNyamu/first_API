from django.http import JsonResponse
from django.shortcuts import render

from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.
def employeeview(request):
    employee = Employee.objects.all()
    serializer = EmployeeSerializer(employee,many=True)
    return JsonResponse({"employee":serializer.data},safe=False)


