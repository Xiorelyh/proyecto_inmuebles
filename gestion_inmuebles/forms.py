from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['tipo_usuario', 'username', 'email', 'rut', 'direccion', 'telefono', 'password1', 'password2']  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo_usuario'].label = "Rol de Usuario"