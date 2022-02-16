#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rest_framework.filters import BaseFilterBackend
import coreapi

class NameFilterBackend(BaseFilterBackend):
    def get_schema_fields(self, view):
        return [coreapi.Field(
            name='user',
            location='query',
            required=False,
            type='integer',
            description='User of the post'
        )]

    def filter_queryset(self, request, queryset, view):
        try:
            n = request.query_params['user']
            queryset = queryset.filter(name=n)
        except KeyError:
            # no query parameters
            pass
        return queryset
