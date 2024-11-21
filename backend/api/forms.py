from django import forms
from .models import Data

# TODO: Class dataform
class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = '__all__'
        widgets = {
            'data_json': forms.HiddenInput(),
        }
        
    
    # TODO: Function save
    def save(self, commit=True, *args, **kwargs):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance
    


