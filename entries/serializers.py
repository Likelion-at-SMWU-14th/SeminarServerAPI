from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Entry

class EntrySerializer(serializers.ModelSerializer):
  author = serializers.StringRelatedField(read_only=True)
  class Meta:
    model = Entry
    fields = ['id', 'author', 'comment', 'timestamp']

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
  def validate(self, attrs):
    data = super().validate(attrs)
    data['username'] = self.user.username
    return data