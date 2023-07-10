

from django.forms import ModelForm


from .models import MenuItems


class MenuItemForm(ModelForm):
    
    class Meta:
        model = MenuItems
        fields = '__all__'