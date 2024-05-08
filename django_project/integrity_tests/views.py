import random
import time

from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django_project.integrity_tests.serializers import CachePostInputSerializer, CachePostOutputSerializer, \
    CacheGetOutputSerializer


class CacheIntegrityView(APIView):
    post_input_serializer = CachePostInputSerializer
    post_output_serializer = CachePostOutputSerializer
    post_status_code = status.HTTP_200_OK

    get_output_serializer = CacheGetOutputSerializer
    get_status_code = status.HTTP_200_OK

    @swagger_auto_schema(
        request_body=post_input_serializer,
        responses={
            post_status_code: post_output_serializer()
        }
    )
    def post(self, request):
        serializer = self.post_input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        cache_data = cache.get(serializer.validated_data['name'])
        if cache_data:
            return Response(cache_data)

        time.sleep(5)

        response_data = {
            'name': serializer.validated_data['name'],
            'random': random.randint(1, 100)
        }

        output = self.post_output_serializer(response_data)

        cache.set(response_data['name'], output.data, timeout=20)

        return Response(data=output.data, status=self.post_status_code)

    @swagger_auto_schema(
        responses={
            get_status_code: get_output_serializer()
        }
    )
    @method_decorator(cache_page(30))
    def get(self, _):
        time.sleep(5)

        response_data = {"random": random.randint(1, 1000)}
        output = self.get_output_serializer(response_data)

        return Response(data=output.data, status=self.get_status_code)
