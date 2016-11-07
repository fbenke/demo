from django import forms
from django.forms import inlineformset_factory

from .models import Setup, Specification


class SetupForm(forms.ModelForm):

    class Meta:
        model = Setup
        fields = '__all__'


class SpecificationForm(forms.ModelForm):

    class Meta:
        model = Specification
        fields = '__all__'

SpecificationFormSet = inlineformset_factory(
    Setup, Specification,
    fields=('result',),
    can_delete=False
)
