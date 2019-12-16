# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import ApplicationModel
from .serializers import ApplicationSerializer, ApplicationKeySerializer


class ApplicationListViewSet(ModelViewSet):
    queryset = ApplicationModel.objects.all()
    serializer_class = ApplicationSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        if 'key' in data:
            data.pop('key')
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)


class ApplicationItemViewSet(ModelViewSet):
    queryset = ApplicationModel.objects.all()
    serializer_class = ApplicationSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.GET.get('key') == instance.key:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            self.permission_denied(self.request)

    def update(self, request, *args, **kwargs):
        data = request.data
        if 'key' in data:
            data.pop('key')
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class ApplicationUpdateKeyViewSet(ModelViewSet):
    queryset = ApplicationModel.objects.all()
    serializer_class = ApplicationKeySerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = {'key': hashlib.md5(instance.name).hexdigest()}
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'key': serializer.data['key']})
