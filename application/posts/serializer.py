from rest_framework import serializers
from .models import SomePosts


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SomePosts
        fields = ('id', 'title', 'image', 'post')

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author_id'] = request.user.id
        post = SomePosts.objects.create(**validated_data)
        return post