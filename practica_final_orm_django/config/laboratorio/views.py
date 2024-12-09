from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Laboratorio, DirectorGeneral, Producto
from .forms import LaboratorioForm, DirectorGeneralForm, ProductoForm

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Laboratorio, DirectorGeneral, Producto
from .forms import LaboratorioForm, DirectorGeneralForm, ProductoForm

# Create your views here.

# views o controller para listar laboratorios
def listar_laboratorios(request):
    laboratorios = Laboratorio.objects.all().order_by('id')
    return render(request, 'listar_laboratorios.html', {'laboratorios': laboratorios})

# views o controller para crear laboratorios
def crear_laboratorio(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Laboratorio creado')
            return redirect('listar_laboratorios')
        else:
            messages.error(request, 'Revisar datos ingresados')
            return HttpResponseRedirect(reverse('crear_laboratorio'))
    else:
        form = LaboratorioForm()
    return render(request, 'crear_laboratorio.html', {'form': form})

# views o controller para editar laboratorios
def editar_laboratorio(request, laboratorio_id):
    laboratorio = get_object_or_404(Laboratorio, id=laboratorio_id)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Laboratorio actualizado con éxito.')
            return redirect('listar_laboratorios')
        else:
            messages.error(request, 'Por favor, corrige los errores del formulario.')
    else:
        form = LaboratorioForm(instance=laboratorio)
    return render(request, 'editar_laboratorio.html', {'form': form, 'laboratorio_id': laboratorio_id})


# views o controller para eliminar laboratorios
def eliminar_laboratorio(request, laboratorio_id):
    laboratorio = get_object_or_404(Laboratorio, id=laboratorio_id) 
    if request.method == 'POST':
        laboratorio.delete()
        messages.success(request, 'Laboratorio eliminado')
        return redirect('listar_laboratorios')
    return render(request, 'eliminar_laboratorio.html', {'laboratorio': laboratorio})


# views o controller para registro
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado con éxito')
            return redirect('login')
        else:
            messages.error(request, 'Error en el registro, revisar datos')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

# views o controller para login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenido {username}')
                return redirect('listar_laboratorios')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')
        else:
            messages.error(request, 'Error en el formulario')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# views o controller para logout
def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada con éxito')
    return redirect('login')

def index(request):
    return render(request, 'index.html')
    
def buscar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        try:
            query_id = int(query)
        except ValueError:
            query_id = None
        productos = Producto.objects.filter(
            Q(nombre__icontains=query) | 
            Q(descripcion__icontains=query) | 
            (Q(id=query_id) if query_id is not None else Q())
            ).order_by('id')
        return render(request, 'listar_productos.html', {'productos':productos})

def listar_productos(request):
    productos = Producto.objects.all().order_by('id')
    return render(request, 'listar_productos.html', {'productos': productos})
    
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado con éxito.')
            return redirect('listar_productos')
        else:
            messages.error(request, 'Por favor, corrige los errores del formulario.')
    else:
        form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form})


def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado con éxito.')
            return redirect('listar_productos')
        else:
            messages.error(request, 'Por favor, corrige los errores del formulario.')
    else:
        form = ProductoForm(instance=producto)
        return render(request, 'editar_producto.html', {'form': form, 'producto_id': producto_id})
    
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado con éxito.')
        return redirect('listar_productos')
    return render(request, 'eliminar_producto.html', {'producto': producto})


