# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from . serializers import UserSerializer, GroupSerializer, FishSerializer, ReportSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class FishAnalysisView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        fish_serializer = FishSerializer(data=request.data)
        if fish_serializer.is_valid():
            fish_serializer.save()
            return Response(fish_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(fish_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BugReportView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        report_serializer = ReportSerializer(data=request.data)
        if report_serializer.is_valid():
            report_serializer.save()
            return Response(report_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(report_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
