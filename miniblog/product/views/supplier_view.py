from django.shortcuts import render, redirect
from product.repositories.supplier import SupplierRepository

def supplier_list (request):
    supplier_repository = SupplierRepository()
    suppliers = supplier_repository.get_all()
    return render(
        request,
        'supplier/list.html',
        dict(
        suppliers=suppliers
    ))

def supplier_delete(request, id:int):
    supplier_repository= SupplierRepository()
    supplier= supplier_repository.get_by_id(id)
    supplier_repository.delete(supplier)
    return redirect ('supplier_list')
    
def supplier_create(request): 
    supplier_repository= SupplierRepository()
    if request.method == "POST":
        nombre = request.POST.get('name')
        direccion = request.POST.get('address')
        telefono = request.POST.get('phone')
        supplier_repository.create(
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
        )
        return redirect('supplier_list')
    return render (
        request,
        'supplier/create.html',
    )

def supplier_detail(request, id:int):
    supplier_repository = SupplierRepository()
    supplier= supplier_repository.get_by_id(id)
    return render(
        request,
        'supplier/detail.html',
        dict(
        supplier=supplier
        )
    )

def supplier_update(request, id:int):
    supplier_repository = SupplierRepository()
    supplier= supplier_repository.get_by_id(id=id)
    if request.method== "POST":
        nombre = request.POST.get('name')
        direccion = request.POST.get('address')
        telefono = request.POST.get('phone')
        supplier_repository.update(
            supplier=supplier,
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
        )
        return redirect ('supplier_list')
    
    return render(
        request,
        'supplier/update.html',
        dict(
            supplier=supplier
        )
    )