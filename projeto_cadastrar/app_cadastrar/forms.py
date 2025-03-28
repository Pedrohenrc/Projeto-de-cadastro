from django import forms
from .models import Usuario

class UsuarioForm (forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['numcard', 'titcard', 'securycard', 'expiry_date']
        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
            'securycard': forms.PasswordInput(render_value=True)
        }