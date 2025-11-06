from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor
from django.urls import reverse
from django.utils import timezone

def inicio_paleteria(request):
    return render(request, 'inicio.html')

# Agregar proveedor
def agregar_proveedor(request):
    if request.method == 'POST':
        nombre_empresa = request.POST.get('nombre_empresa', '')
        contacto = request.POST.get('contacto', '')
        telefono = request.POST.get('telefono', '')
        email = request.POST.get('email', '')
        direccion = request.POST.get('direccion', '')
        ciudad = request.POST.get('ciudad', '')
        # Creación sencilla sin validaciones
        Proveedor.objects.create(
            nombre_empresa=nombre_empresa,
            contacto=contacto,
            telefono=telefono,
            email=email,
            direccion=direccion,
            ciudad=ciudad,
            fecha_registro=timezone.now().date()
        )
        return redirect('ver_proveedor')
    return render(request, 'proveedor/agregar_proveedor.html')

# Ver proveedores (tabla)
def ver_proveedor(request):
    proveedores = Proveedor.objects.all().order_by('id_proveedor')
    return render(request, 'proveedor/ver_proveedor.html', {'proveedores': proveedores})

# Mostrar formulario de actualización
def actualizar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    return render(request, 'proveedor/actualizar_proveedor.html', {'proveedor': proveedor})

# Realizar la actualización
def realizar_actualizacion_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.nombre_empresa = request.POST.get('nombre_empresa', proveedor.nombre_empresa)
        proveedor.contacto = request.POST.get('contacto', proveedor.contacto)
        proveedor.telefono = request.POST.get('telefono', proveedor.telefono)
        proveedor.email = request.POST.get('email', proveedor.email)
        proveedor.direccion = request.POST.get('direccion', proveedor.direccion)
        proveedor.ciudad = request.POST.get('ciudad', proveedor.ciudad)
        proveedor.save()
        return redirect('ver_proveedor')
    return redirect('ver_proveedor')

# Borrar proveedor (confirmación)
def borrar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('ver_proveedor')
    return render(request, 'proveedor/borrar_proveedor.html', {'proveedor': proveedor})
