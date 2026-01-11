from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import EmployeeProfile, AttendanceRecord
from .serializers import EmployeeSerializer, AttendanceSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceSerializer



@api_view(["GET"])
def healthz(request):
    return Response({
        "status": "ok",
        "message": "hello world updated thanks"
    })
