from rest_framework import serializers

from .models import TinyUrl


class TinyUrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = TinyUrl
        fields = ('id', 'tiny_id', 'original_url', 'expires_on', 'last_used_on',)
        read_only_fields = ('id', 'tiny_id', 'original_url', 'expires_on', 'last_used_on',)


class TinyUrlCreateSerializer(serializers.ModelSerializer):
    tiny_id = serializers.CharField(required=False, max_length=10, min_length=8)
    original_url = serializers.URLField(required=True)

    class Meta:
        model = TinyUrl
        fields = ('id', 'tiny_id', 'original_url', 'expires_on', 'last_used_on',)
        read_only_fields = ()

    def validate(self, attrs):
        tiny_id = attrs.get('tiny_id')

        # Check if the tiny_id does not already exist
        if tiny_id and TinyUrl.objects.filter(tiny_id=tiny_id).exists():
            raise serializers.ValidationError({
                'tiny_id': 'Tiny Id already exists. Please try a different id.'
            })

        return attrs

    def get_tiny_id(self, tiny_url):
        tiny_id = tiny_url.generate_key()
        if TinyUrl.objects.filter(tiny_id=tiny_id).exists():
            tiny_id = self.get_tiny_id(tiny_url)

        return tiny_id

    def create(self, validated_data):
        tiny_url = None
        if validated_data.get('tiny_id'):
            tiny_url = TinyUrl(
                tiny_id=validated_data.get('tiny_id'),
                original_url=validated_data.get('original_url'),
            )
        else:
            tiny_url = TinyUrl(
                original_url=validated_data.get('original_url'),
            )
            tiny_url.tiny_id = self.get_tiny_id(tiny_url)

        tiny_url.save()
        return tiny_url
