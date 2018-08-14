from rest_framework import serializers
from . import models


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('user_id', 'message_id', 'datetime','sender','message_text', 'created_at', 'updated_at',)
        model = models.Message