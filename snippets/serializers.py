from django.contrib.auth.models import User
from rest_framework.serializers import (
    HyperlinkedModelSerializer, ReadOnlyField,
    HyperlinkedIdentityField, HyperlinkedRelatedField,
)
from .models import Snippet


class SnippetSerializer(HyperlinkedModelSerializer):
    owner = ReadOnlyField(source='owner.username')
    highlight = HyperlinkedIdentityField(view_name='snippet-highlight',
                                         format='html')

    class Meta:
        model = Snippet
        fields = (
            'url', 'id', 'highlight', 'owner',
            'title', 'code', 'linenos', 'language', 'style',
        )


class UserSerializer(HyperlinkedModelSerializer):
    snippets = HyperlinkedRelatedField(many=True, view_name='snippet-detail',
                                       read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')
