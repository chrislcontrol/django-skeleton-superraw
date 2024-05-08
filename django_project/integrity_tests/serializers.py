from rest_framework import serializers


class CachePostInputSerializer(serializers.Serializer):
    name = serializers.CharField()


class CachePostOutputSerializer(serializers.Serializer):
    name = serializers.CharField()
    random = serializers.IntegerField()


class CacheGetOutputSerializer(serializers.Serializer):
    random = serializers.IntegerField()
