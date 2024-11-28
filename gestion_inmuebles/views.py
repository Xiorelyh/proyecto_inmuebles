from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import BuscadorForm
from .models import Inmueble
from .forms import RegistroUsuarioForm
from django.contrib.auth.decorators import login_required


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


@login_required
def perfil_usuario(request):
    if request.user.tipo_usuario == 'arrendador':  # Verifica el tipo de usuario
        return render(request, 'perfil_arrendador.html')
    elif request.user.tipo_usuario == 'arrendatario':
        return render(request, 'perfil_arrendatario.html')
    else:
        return render(request, 'error.html', {'mensaje': 'Tipo de usuario no reconocido'})
    

#Paga_ Arriendo

def paga_tu_arriendo(request):
    return render(request, 'paga_tu_arriendo.html')


def perfil_arrendatario(request):
    user = request.user
    propiedades_favoritas = user.propiedades_favoritas.all()

    if request.method == "POST":
        form = PerfilForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('perfil_arrendatario')
    else:
        form = PerfilForm(instance=user)

    return render(request, 'perfil_arrendatario.html', {
        'form': form,
        'propiedades_favoritas': propiedades_favoritas
    })

# Agendar Visita
def agendar_visita(request):
    if request.method == "POST":
        form = VisitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('perfil_arrendatario')
    else:
        form = VisitaForm()

    return render(request, 'agendar_visita.html', {'form': form})


#Editar Perfil

@login_required
def editar_perfil(request):
    user = request.user  # Usuario actualmente autenticado
    if request.method == 'POST':
        user.nombre = request.POST.get('nombre', user.nombre)
        user.email = request.POST.get('email', user.email)
        user.telefono = request.POST.get('telefono', user.telefono)
        user.direccion = request.POST.get('direccion', user.direccion)

        # Manejo de foto de perfil
        if 'foto_perfil' in request.FILES:
            user.foto_perfil = request.FILES['foto_perfil']

        user.save()
        messages.success(request, 'Perfil actualizado exitosamente.')
        return redirect('editar_perfil')

    return render(request, 'editar_perfil.html', {'user': user})

