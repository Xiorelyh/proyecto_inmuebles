from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import BuscadorForm
from .models import Inmueble
from .forms import RegistroUsuarioForm
from .forms import PropiedadForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse 
from .models import Inmueble, Favorito
from django.contrib.auth.decorators import login_required
from .models import Favorito


def inicio(request):
    form = BuscadorForm(request.GET)  
    resultados = Inmueble.objects.all()  
    
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
            form.save()  
            messages.success(request, 'Usuario registrado con éxito.')
            # Autenticar al usuario después del registro
            usuario = authenticate(username=form.cleaned_data['username'], 
                                   password=form.cleaned_data['password1'])
            if usuario is not None:
                login(request, usuario)
                return redirect('inicio')  # Redirige a la página principal
        else:
            messages.error(request, 'Error al registrar el usuario. Revisa los datos ingresados.')
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'registro.html', {'form': form})


@login_required
def perfil_usuario(request):
    if request.user.tipo_usuario == 'arrendador':
        propiedades_publicadas = Inmueble.objects.filter(arrendador=request.user)
        return render(request, 'perfil_arrendador.html', {'propiedades_publicadas': propiedades_publicadas})
    
    elif request.user.tipo_usuario == 'arrendatario':
        propiedades_favoritas = Favorito.objects.filter(usuario=request.user).select_related('inmueble')
        return render(request, 'perfil_arrendatario.html', {'propiedades_favoritas': propiedades_favoritas})

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
    user = request.user

    if request.method == 'POST':
        user.username = request.POST.get('nombre', user.username)
        user.email = request.POST.get('email', user.email)
        user.telefono = request.POST.get('telefono', user.telefono)
        user.direccion = request.POST.get('direccion', user.direccion)
        user.rut = request.POST.get('rut', user.rut)  

        user.save()  # Guarda los cambios

        messages.success(request, "Tu perfil ha sido actualizado con éxito.")

    return render(request, 'editar_perfil.html', {'user': user})

#Inmuebles Favoritos
@login_required
def agregar_favorito(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, id=inmueble_id) 
    favorito, created = Favorito.objects.get_or_create(usuario=request.user, inmueble=inmueble)
    
    if created:
        print(f"{inmueble.nombre} agregado a favoritos")
    else:
        print(f"{inmueble.nombre} ya estaba en favoritos")
    
    return HttpResponseRedirect(reverse('perfil_usuario'))


#Publicar Propiedad
@login_required
def publicar_propiedad(request):
    if request.method == 'POST':
        form = PropiedadForm(request.POST, request.FILES)
        if form.is_valid():
            nueva_propiedad = form.save(commit=False)
            nueva_propiedad.arrendador = request.user  
            nueva_propiedad.save()
            messages.success(request, 'Propiedad publicada con éxito.')
            return redirect('perfil_usuario')
    else:
        form = PropiedadForm()
    return render(request, 'publicar_propiedad.html', {'form': form})


#Editar Propiedd
@login_required
def editar_propiedad(request, propiedad_id):
    propiedad = Inmueble.objects.get(id=propiedad_id, arrendador=request.user)
    if request.method == 'POST':
        form = PropiedadForm(request.POST, instance=propiedad)
        if form.is_valid():
            form.save()
            return redirect('perfil_usuario')
    else:
        form = PropiedadForm(instance=propiedad)
    return render(request, 'editar_propiedad.html', {'form': form, 'propiedad': propiedad})


#Vista del Inmueble
def detalle_inmueble(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    return render(request, 'detalle_inmueble.html', {'inmueble': inmueble})