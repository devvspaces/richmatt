from django import forms

from .models import Gallery


class FilterForm(forms.ModelForm):
    category = forms.ChoiceField(required=False, choices = Gallery.CATEGORY, widget=forms.Select(attrs={'class':'form-select'}))

    class Meta:
    	model = Gallery
    	fields = ('category',)


class CreateForm(forms.ModelForm):
    category = forms.ChoiceField(choices = Gallery.CATEGORY, widget=forms.Select(attrs={'class':'form-select'}))
    caption = forms.CharField(required=False, max_length=50, widget=forms.Textarea(attrs={'class':'form-control'}))
    picture = forms.ImageField()

    class Meta:
    	model = Gallery
    	fields = ('category','picture','caption',)