from django import forms
from api.models import Data, Host
from api.utils import hash_person

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
    
    
# TODO: Class dataform
class HostForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = '__all__'
        widgets = {
            'host_password': forms.PasswordInput(),
        }
        
    
    # TODO: Function save
    def save(self, commit=True, *args, **kwargs):
        # Cria uma instância do objeto Host sem salvar
        instance = super().save(commit=False)
        
        if self.cleaned_data.get("host_password"):
            instance.host_password = hash_person.PasswordFernetKey.make_hash(self.cleaned_data["host_password"])

        if commit:
            instance.save()
        
        return instance



