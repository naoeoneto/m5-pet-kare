from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from groups.models import Group
# from rest_framework.views import status

# class CustomValidationException(UniqueValidator):
#     default_code = 'group already registered.'
    
#     def __init__(self, detail=None):
#         super().__init__(detail, code=self.default_code, status_code=status.HTTP_200_OK)

class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    scientific_name = serializers.CharField(
        max_length=50,
        validators=[
            UniqueValidator(Group.objects.all(), message="group already registered.")
        ],
    )
    created_at = serializers.DateTimeField(read_only=True)
