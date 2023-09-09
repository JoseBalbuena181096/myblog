from django import forms
# Importar modelo de subscripción
from .models import Suscribers, Contact


class SuscribersForms(forms.ModelForm):
    class Meta:
        model = Suscribers
        fields  = ('email',)
        widgets = {
            'email' : forms.EmailInput(
                attrs = {
                    'placeholder': 'Ingrese email',
                    'class' : 'input-email'
                }
            ),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('__all__')