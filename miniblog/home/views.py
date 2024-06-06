from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import View

class LoginView(View):
    
    def get(self, requests):
        return render (
            requests, 
            'home/login.html',
            )
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate( #validar si existe ese usuario con esa contraseña
                request,
                username=username,
                password=password,
            )
            if user:
                login(request,user)
                return redirect('index') #si el usuario esta registrado
        return redirect('login') #si no esta registrado
       

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('login')




#tiene que estar logeado para entrar si o si, sino vuelve al login
@login_required(login_url='login')
def index_view(request): #vista
    return render(
        request,
        'home/index.html'
    )

