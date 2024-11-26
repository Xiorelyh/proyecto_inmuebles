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
            # Validación de contraseñas
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            
            if password1 != password2:
                messages.error(request, 'Las contraseñas no coinciden.')
            else:
                usuario = form.save(commit=False)
                usuario.set_password(password1)  # Establece la contraseña en el usuario
                usuario.save()

                messages.success(request, 'Usuario registrado con éxito.')

                # Autenticar al usuario después del registro
                usuario_autenticado = authenticate(username=usuario.username, password=password1)
                if usuario_autenticado is not None:
                    login(request, usuario_autenticado)
                    return redirect('inicio')  # Redirige al inicio después del login
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'registro.html', {'form': form})

