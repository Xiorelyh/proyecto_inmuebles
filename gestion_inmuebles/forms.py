from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from .models import Inmueble
from .models import Usuario, Visita
from .models import Comuna, Tipo_inmueble

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


class PropiedadForm(forms.ModelForm):

    comuna = forms.ModelChoiceField(queryset=Comuna.objects.all(), empty_label="Seleccione una comuna", required=True)
    tipo_inmueble = forms.ModelChoiceField(queryset=Tipo_inmueble.objects.all(), empty_label="Seleccione un tipo de inmueble", required=True)

    class Meta:
        model = Inmueble
        fields = ['nombre', 'descripcion', 'm2_construidos', 'm2_totales', 
                  'estacionamientos', 'habitaciones', 'banos', 
                  'direccion', 'comuna', 'tipo_inmueble', 'precio_mensual', 'imagen']