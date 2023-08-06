from django import forms
from .models import Festival


class FestivalForm(forms.ModelForm):

    class Meta:
        model = Festival
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
