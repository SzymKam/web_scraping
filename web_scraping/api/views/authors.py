from data_processing.models import WordCount
from rest_framework.response import Response
from rest_framework.views import APIView


class AuthorListView(APIView):
    @staticmethod
    def get(request):
        authors = WordCount.objects.values("author", "author_lowercase").distinct()
        authors_list = {}
        for author in authors:
            authors_list[author["author_lowercase"]] = author["author"]

        return Response(authors_list)
