from django import forms
from django.shortcuts import get_object_or_404

from .models import Product


class FilterForm(forms.ModelForm):
    # category = mod
    category = forms.ChoiceField(required=False, choices = Product.CATEGORY, widget=forms.Select(attrs={'class':'form-select'}))
    min_price = forms.FloatField(required=False, widget=forms.NumberInput(attrs={'class':'form-control'}))
    max_price = forms.FloatField(required=False, widget=forms.NumberInput(attrs={'class':'form-control'}))

    class Meta:
    	model = Product
    	fields = ('category',)

    def clean(self):
    	cleaned_data = super(FilterForm, self).clean()

    	min_price = cleaned_data.get('min_price')
    	max_price = cleaned_data.get('max_price')

    	if min_price and max_price:
    		if min_price > max_price:
    			self.add_error('min_price', 'Min price should be lower than Max price')

    	return cleaned_data


class CreateForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    category = forms.ChoiceField(choices = Product.CATEGORY, widget=forms.Select(attrs={'class':'form-select'}))
    old_price = forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    new_price = forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    picture = forms.ImageField()

    class Meta:
        model = Product
        fields = ('name','category','old_price','new_price','picture',)