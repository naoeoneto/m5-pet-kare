from rest_framework.views import APIView, Request, Response, status
from rest_framework.pagination import PageNumberPagination
from .serializers import PetSerializer
from .models import Pet
from groups.models import Group
from traits.models import Trait


class PetView(APIView, PageNumberPagination):
    def post(self, request: Request) -> Response:
        serializer = PetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        traits = serializer.validated_data.pop("traits")
        group = serializer.validated_data.pop("group")
        group_obj = Group.objects.filter(scientific_name__iexact=group["scientific_name"]).first()
        
        if not group_obj:
            group_obj = Group.objects.create(**group)

        pet_obj = Pet.objects.create(**serializer.validated_data, group=group_obj)

        for trait_dict in traits:
            trait_obj = Trait.objects.filter(name__iexact=trait_dict["name"]).first()

            if not trait_obj:
                trait_obj = Trait.objects.create(**trait_dict)
        
            pet_obj.traits.add(trait_obj)
        
        serializer = PetSerializer(pet_obj)

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        pets = Pet.objects.all().order_by('id')
        result_page = self.paginate_queryset(pets, request)
        serializer = PetSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)
