from typing import List, Optional, NoReturn
from product.models import Supplier

class SupplierRepository:
    def get_all(self) -> List[Supplier]:
           return Supplier.objects.all()

    def create(
        self,
        nombre: str,
        direccion:str,
        telefono:int,

    ) -> Supplier:
        supplier= Supplier.objects.filter(name=nombre)
        
        return Supplier.objects.create(
            name=nombre,
            address=direccion,
            phone=telefono,
        )
    
    def get_by_id(self, id: int) -> Optional[Supplier]:
        return Supplier.objects.get(id=id)
    
    def delete(self, supplier: Supplier):
        supplier.delete()

    def update(
        self, 
        supplier: Supplier,
        nombre:str,
        direccion:str,
        telefono:int,
        ):
          supplier.name=nombre
          supplier.address=direccion
          supplier.phone=telefono
          supplier.save()