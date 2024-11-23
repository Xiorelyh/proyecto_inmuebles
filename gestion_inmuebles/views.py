from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegistroUsuarioForm

# Vista principal que carga todos los flanes
def inicio(request):
    return render(request, 'index.html')

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
