from rest_framework import serializers
from . import models
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','title','description','created_at','updated_at',)
        model=models.Notemodel