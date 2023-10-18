from data_processing.models import WordCount
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers.top_10_serializer import Top10Serializer


class Top10ByAuthorView(APIView):
    @staticmethod
    def get(request, author: str):
        word_counts_by_author = (
            WordCount.objects.filter(author_lowercase=author)
            .values("word")
            .annotate(count=Sum("count"))
            .order_by("-count")[:10]
        )

        serializer = Top10Serializer(word_counts_by_author, many=True)

        return Response(serializer.data)
