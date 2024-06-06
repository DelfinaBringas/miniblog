from django.urls import path

from home.views import(
    index_view,
    LoginView,
    LogoutView,
)

urlpatterns=[
    path('', view=index_view, name='index'),
    path(route='login/', view=LoginView.as_view(), name='login'), #para traer los metodos de la clase
    path(route='logout/', view=LogoutView.as_view(), name='logout'),
]