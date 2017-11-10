from rest_framework import serializers

from .models import Translation


class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = (
            'pre_translated_text',
            'post_translated_text',
        )
        read_only_fields = (
            'post_translated_text',
        )
