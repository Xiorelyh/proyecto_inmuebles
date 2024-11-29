"""
URL configuration for proyecto_inmuebles project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from gestion_inmuebles import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name="inicio"),
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('perfil/<int:inmueble_id>/', views.perfil_usuario, name='perfil_usuario_detalle'),
    path('pagar-arriendo/', views.paga_tu_arriendo, name='paga_tu_arriendo'),
    path('agendar-visita/', views.agendar_visita, name='agendar_visita'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('agregar_favorito/<int:inmueble_id>/', views.agregar_favorito, name='agregar_favorito'),
    path('propiedades/publicar/', views.publicar_propiedad, name='publicar_propiedad'),
    path('propiedades/editar/<int:propiedad_id>/', views.editar_propiedad, name='editar_propiedad'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)