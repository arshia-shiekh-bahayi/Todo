from rest_framework import serializers
from Todo.models import *
"""A serializer class that can be used to serialize a post"""


class TaskSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(
        source='get_absolute_api_url', read_only=True)
    absolute_url = serializers.SerializerMethodField(method_name='get_abs_url')
    author_name = serializers.SerializerMethodField(
        method_name='author_real_name')

    class Meta:
        model = Task
        fields = ['id', 'author', 'author_name', 'title', 'snippet', 'content',
                  'status', 'relative_url', 'absolute_url', 'created_date', 'updated_date']
        read_only_fields = ['author']

    def create(self, validated_data):
        validated_data['author'] = Profile.objects.get(
            user__id=self.context.get('request').user.id)
        return super().create(validated_data)

    def get_abs_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)

    def author_real_name(self, obj):
        prof = obj.author
        prof = str(prof)
        return prof

    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('snippet', None)
            rep.pop('relative_url', None)
            rep.pop('absolute_url', None)
        else:
            rep.pop('content', None)
        return rep
