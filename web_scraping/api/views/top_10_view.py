from data_processing.models import WordCount
from django.db.models import Count, Sum
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers.top_10_serializer import Top10Serializer


class Top10View(APIView):
    @staticmethod
    def get(request):
        word_counts = WordCount.objects.values("word").annotate(count=Sum("count")).order_by("-count")[:10]

        serializer = Top10Serializer(word_counts, many=True)
        print(serializer.data)
        return Response(serializer.data)
