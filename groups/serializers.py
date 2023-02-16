from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from groups.models import Group


class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    scientific_name = serializers.CharField(
        max_length=50,
        # validators=[
        #     UniqueValidator(Group.objects.all(), message="group already registered.")
        # ],
    )
    created_at = serializers.DateTimeField(read_only=True)
