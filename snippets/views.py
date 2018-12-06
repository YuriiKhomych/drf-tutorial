from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetList(ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(RetrieveDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
