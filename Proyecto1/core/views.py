from django.shortcuts import render, redirect
# Create your views here.

from django.contrib.auth import authenticate, login
from .forms import CustomUserForm, UserCreationForm
def home(request):
    return render(request, 'core/Paginaprincipal.html')

def registro(request):
    data={
        'form':CustomUserForm()
    }
    if request.method=='POST':
        formulario = CustomUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()

            username=formulario.cleaned_data['username']
            password=formulario.cleaned_data['password1']
            user=authenticate(username=username, password=password)
            login(request,user)
            return redirect (to='home')
    return render(request,'registration/registro.html',data)



def Registrar(request):
    return render(request, 'core/Registrar.html')    

def Formulario(request):
    return render(request, 'core/Formulario.html')

def pintura(request):
    return render(request, 'core/pintura.html')

def ruedas(request):
    return render(request, 'core/ruedas.html')
    
def motor(request):
    return render(request, 'core/motor.html')

def interior(request):
    return render(request, 'core/interior.html')    

def frenos(request):
    return render(request, 'core/frenos.html')

def Iniciarsesion(request):
    return render(request, 'core/Iniciarsesion.html')    


    



    






