from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('',include("home.urls")), #raiz del proyecto
    path('admin/', admin.site.urls),
    path('products/', include("product.urls")), #la ruta q empiexe con products, trae todas
    #las rutas de urls products
]