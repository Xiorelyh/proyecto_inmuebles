from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from .models import Inmueble
from .models import Usuario, Visita


class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['tipo_usuario', 'username', 'email', 'rut', 'direccion', 'telefono', 'password1', 'password2']  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo_usuario'].label = "Rol de Usuario"

class BuscadorForm(forms.Form):
    tipo_inmueble = forms.ChoiceField(
        choices=[('', 'Todos')] + [(tipo, tipo) for tipo in ['Casa', 'Departamento', 'Oficina', 'Bodega']],
        required=False,
        label="Tipo de Propiedad"
    )
    comuna = forms.ChoiceField(
        choices=[('', 'Todas las comunas')] + [(comuna, comuna) for comuna in Inmueble.objects.values_list('comuna', flat=True).distinct()],
        required=False,
        label="Comuna"
    )

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'telefono', 'foto_perfil']

class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ['inmueble', 'fecha_visita']

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'telefono', 'direccion', 'foto_perfil']  