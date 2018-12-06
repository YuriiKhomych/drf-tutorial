from django.contrib.auth.models import User
from rest_framework.serializers import (
    ModelSerializer, PrimaryKeyRelatedField, ReadOnlyField
)
from .models import Snippet


class SnippetSerializer(ModelSerializer):
    owner = ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = (
            'id', 'title', 'code', 'linenos',
            'language', 'style', 'owner',
        )


class UserSerializer(ModelSerializer):
    snippets = PrimaryKeyRelatedField(many=True,
                                      queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
