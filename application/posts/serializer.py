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

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SomePosts
        fields = ('image', )

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
                print(url)
        else:
            url = ''
        return url


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation


