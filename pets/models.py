from django.db import models


class CategoryPets(models.TextChoices):
    MALE = 'Male',
    FEMALE = 'Female',
    DEFAULT = 'Not Informed'


class Pet(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.DecimalField(decimal_places=2, max_digits=5)
    sex = models.CharField(
        max_length=20, 
        choices=CategoryPets.choices, 
        default=CategoryPets.DEFAULT
    )
    group = models.ForeignKey('groups.Group', on_delete=models.PROTECT, related_name='pets')

    def __repr__(self) -> str:
        return f'<Pet - [{self.id}] - {self.name}'
