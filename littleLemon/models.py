from django.db import models

# Create your models here.



class MenuItems(models.Model):

    CATEGORIES = [
        ("I", "Italian"),
        ("G", "Greek"),
        ("F", "French"),
    ]

    COURSE = [
        ('SA', 'Salads'),
        ('MC', 'Main Course'),
        ('DS', 'Dessert'),
        #('HO', "Hors-d'oeuvres"),
        #('AB', "Amuse-bouche"),
        ('SO', "Soup"),
        ("FI", "Fish"),
        ("CH", "Cheese plate"),
        ("AP", "Antipasti"),
        ("MZ", "Mezes")
    ]

    item = models.CharField(max_length = 250)
    description = models.CharField(max_length=250)
    category = models.CharField(max_length=1, choices=CATEGORIES, default="G")
    course = models.CharField(max_length=2, choices=COURSE, default="MC")


    def __str__(self):
        return f'{self.item}'


    class Meta:

        verbose_name_plural = 'MenuItems'