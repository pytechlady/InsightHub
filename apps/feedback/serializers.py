from .models import Dataset
from rest_framework.serializers import Serializer


class DatasetSerializer(Serializer.ModelSerializer):
    class Meta:
        model = Dataset
        fields = '__all__'
        read_only_fields = ['uploaded_by', 'uploaded_at', 'is_processed']