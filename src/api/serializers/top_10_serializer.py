from rest_framework import serializers


class Top10Serializer(serializers.Serializer):
    word = serializers.CharField()
    count = serializers.IntegerField()
