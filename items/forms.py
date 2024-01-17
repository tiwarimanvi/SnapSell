from django import forms

from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')

        category = forms.ChoiceField(widget=forms.Select(attrs={
        'placeholder': 'category',
        'class': 'w-full py-4 px-6 rounded-xl border'
    }))
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'name',
        'class': 'w-full py-4 px-6 rounded-xl border'
    }))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'description',
        'class': 'w-full py-4 px-6 rounded-xl border'
    }))
    price = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'price',
        'class': 'w-full py-4 px-6 rounded-xl border'
    }))
    image = forms.FileField(widget=forms.FileInput(attrs={
        'placeholder': 'image',
        'class': 'w-full py-4 px-6 rounded-xl border'
    }))


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'name',
        'class': 'w-full py-4 px-6 rounded-xl border'
    }))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'description',
        'class': 'w-full py-4 px-6 rounded-xl border'
    }))
    price = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'price',
        'class': 'w-full py-4 px-6 rounded-xl border'
    }))
    image = forms.FileField(widget=forms.FileInput(attrs={
        'placeholder': 'image',
        'class': 'w-full py-4 px-6 rounded-xl border'
    }))