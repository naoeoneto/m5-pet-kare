from rest_framework import serializers
from .models import CategoryPets
from groups.serializers import GroupSerializer
from traits.serializers import TraitSerializer

class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.DecimalField(decimal_places=2, max_digits=5)
    sex = serializers.ChoiceField(
        choices=CategoryPets.choices, 
        default=CategoryPets.NOT_INFORMED
    )
    group = GroupSerializer()
    traits = TraitSerializer(read_only=True, many=True)
