from django import forms
from django.contrib.auth import authenticate
#
from .models import User

class UserRegisterForm(forms.ModelForm):

    email = forms.EmailField(
        label='Ingrese email:',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'email',
                'class':"custom-rounding",
            }
        )
    )

    full_name = forms.CharField(
        label='Nombre completo:',
        required=True,
        widget= forms.TextInput(
            attrs={
                'placeholder': 'nombre completo:',
                'class':"custom-rounding",
            }
        )
    )

    ocupation  = forms.CharField(
        label='ocupación:',
        required=True,
        widget= forms.TextInput(
            attrs={
                'placeholder': 'Ocupación:',
                'class':"custom-rounding",
            }
        )
    )

    genero  = forms.ChoiceField(
        label='genero:',
        required=True,
        choices = User.GENDER_CHOICES,
        widget= forms.Select(
            attrs={
                'class':"custom-rounding",
            }
        )
    )

    date_birth  = forms.DateField(
        required=True,
        widget= forms.DateInput(
            attrs={
                'type': 'date',
                'class':"custom-rounding",
            }
        )
    )

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña',
                'class':"custom-rounding",
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir Contraseña',
                'class':"custom-rounding",
            }
        )
    )

    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = (
            'email',
            'full_name',
            'ocupation',
            'genero',
            'date_birth',
        )
    
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no son iguales')


class LoginForm(forms.Form):
    email = forms.CharField(
        label='E-mail',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Correo Electronico',
                'class':"custom-rounding",
            }
        )
    )
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'contraseña',
                'class':"custom-rounding",
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Los datos de usuario no son correctos')
        
        return self.cleaned_data


class UpdatePasswordForm(forms.Form):
    password1 = forms.CharField(
        label='Ingrese contraseña actual:',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña actual'
            }
        )
    )
    password2 = forms.CharField(
        label='Ingrese contraseña nueva: ',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                 'placeholder': 'Contraseña nueva'
            }
        )
    )
    password3 = forms.CharField(
        label='Repita contraseña nueva: ',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                 'placeholder': 'Repita contraseña nueva'
            }
        )
    )

    def clean_password3(self):
        password_new = self.cleaned_data['password2']
        password_new_rep = self.cleaned_data['password3']
        if len(password_new) > 0:
            if password_new != password_new_rep:
                print(password_new)
                print(password_new_rep)
                raise forms.ValidationError('Las contraseñas son diferentes intente de nuevo')    
        else:
            raise forms.ValidationError('Las contraseñas estan vacías ') 
        return self.cleaned_data


class VerificationForm(forms.Form):

    codregistro = forms.CharField(
        label='Ingrese código de verificación:',
        required=True,
        widget= forms.TextInput(
            attrs={
                'placeholder': 'Ingrese código',
                'class':"custom-rounding",
            }
        )
    )

    # recivo el pk desde la vista
    def __init__(self,pk, *args, **kwargs):
        self.id_user = pk
        super(VerificationForm, self).__init__(*args, **kwargs)

    def clean_codregistro(self):
        codigo = self.cleaned_data['codregistro']

        if len(codigo) == 6:
            # verificamos si el codigo e id del usuario son validos
            activo = User.objects.cod_validation(
                self.id_user,
                codigo
            )
            if not activo:
                raise forms.ValidationError('el código es incorrecto')    
        else:
            raise forms.ValidationError('el código es incorrecto') 