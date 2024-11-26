from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import BuscadorForm
from .models import Inmueble
from .forms import RegistroUsuarioForm


def inicio(request):
    form = BuscadorForm(request.GET)  # Usamos request.GET para obtener los datos del formulario
    resultados = Inmueble.objects.all()  # Mostrar todos los inmuebles inicialmente

    # Filtrar según los valores seleccionados en el formulario
    if form.is_valid():
        tipo_inmueble = form.cleaned_data.get('tipo_inmueble')
        comuna = form.cleaned_data.get('comuna')

        if tipo_inmueble:
            resultados = resultados.filter(tipo_inmueble=tipo_inmueble)

        if comuna:
            resultados = resultados.filter(comuna=comuna)

    return render(request, 'index.html', {'form': form, 'resultados': resultados})



def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda directamente el usuario, incluido el hashing de la contraseña
            messages.success(request, 'Usuario registrado con éxito.')

            # Autenticar al usuario después del registro
            usuario = authenticate(username=form.cleaned_data['username'], 
                                   password=form.cleaned_data['password1'])
            if usuario is not None:
                login(request, usuario)
                return redirect('inicio')  # Redirige a la página principal
        else:
            # Agrega un mensaje de error si el formulario no es válido
            messages.error(request, 'Error al registrar el usuario. Revisa los datos ingresados.')
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'registro.html', {'form': form})

