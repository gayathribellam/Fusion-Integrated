from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .models import LeaveRequest
from .serializers import LeaveRequestSerializer


class LeaveRequestListView(generics.ListCreateAPIView):
    serializer_class = LeaveRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return LeaveRequest.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LeaveRequestDetailView(generics.RetrieveUpdateAPIView):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return LeaveRequest.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        if serializer.validated_data.get('status') not in ['pending', 'approved', 'rejected']:
            raise ValidationError("Invalid status update.")
        serializer.save()
