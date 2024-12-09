from django.urls import path
from . import views
from .views import index, listar_laboratorios, crear_laboratorio, editar_laboratorio, eliminar_laboratorio, registro, login_view, logout_view, listar_productos, buscar, editar_producto, crear_producto, listar_productos, eliminar_producto

urlpatterns = [
    path('', index, name='index'),
    path('listar_laboratorios/', listar_laboratorios, name='listar_laboratorios'),
    path('crear_laboratorio/', crear_laboratorio, name='crear_laboratorio'),
    path('editar_laboratorio/<int:laboratorio_id>/', editar_laboratorio, name='editar_laboratorio'),
    path('eliminar_laboratorio/<int:laboratorio_id>/', eliminar_laboratorio, name='eliminar_laboratorio'),
    path('registro/', registro, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('listar_productos/', listar_productos, name='listar_productos'),
    path('crear_producto/', crear_producto, name='crear_producto'),
    path('editar_producto/<int:producto_id>/', editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),
    path('buscar/', buscar, name='buscar'),
    
]

