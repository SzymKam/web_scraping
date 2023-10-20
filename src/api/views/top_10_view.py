from django.db.models import Count, Sum
from rest_framework.response import Response
from rest_framework.views import APIView

from data_processing.models import WordCount

from ..serializers.top_10_serializer import Top10Serializer


class Top10View(APIView):
    @staticmethod
    def get(request) -> Response:
        word_counts = WordCount.objects.values("word").annotate(count=Sum("count")).order_by("-count")[:10]

        serializer = Top10Serializer(word_counts, many=True)

        return Response(serializer.data)
