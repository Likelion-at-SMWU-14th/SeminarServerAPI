from rest_framework import serializers
from .models import Entry

class EntrySerializer(serializers.ModelSerializer):
  author = serializers.StringRelatedField(read_only=True)
  class Meta:
    model = Entry
    fields = ['id', 'author', 'comment', 'timestamp']