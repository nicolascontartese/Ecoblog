from multiprocessing import context
from pickle import EMPTY_TUPLE
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, resolve_url
from django.http import HttpResponse
from app1.models import Avatar, Blog
from app1.forms import   UserRegisterForm, UserRegisterForm,UserEditForm
from django.contrib.auth.forms import UserChangeForm


# @login_required
# def inicio2(request):
#       avatares = Avatar.objects.filter(user=request.user.id)
#       return render(request, "app1/inicio2.html", {"url": avatares[0].imagen.url})
      
def inicio(request):
      avatares = Avatar.objects.filter(user=request.user.id).exists()
      
      if  request.user.is_authenticated and avatares == True:
            avatares = Avatar.objects.filter(user=request.user.id)
            return render(request, "app1/inicio.html", {"url": avatares[0].imagen.url})
            
      else: 
            avatares = False   
            return render(request, "app1/inicio.html", {'avatar': avatares})
      
      
def nosotros(request):
      avatares = Avatar.objects.filter(user=request.user.id).exists()
      print(avatares)
      if  request.user.is_authenticated and avatares == True :
            avatares = Avatar.objects.filter(user=request.user.id)
            print(1)
            return render(request, "app1/nosotros.html", {"url": avatares[0].imagen.url})
           
            
      else:
            return render(request, "app1/nosotros.html")

@login_required
def blog(request):
      blog = Blog.objects.all()
      avatares = Avatar.objects.filter(user=request.user.id).exists()
      
      if  request.user.is_authenticated and avatares == True:
            
            blog = Blog.objects.all()
            avatares = Avatar.objects.filter(user=request.user.id)
            return render(request, "app1/blog.html", {"url": avatares[0].imagen.url,'blog': blog})
      else:
            
            return render(request, "app1/blog.html", {'blog': blog})
      

def login_request(request):
      
      
      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)
            
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')
                  
                  user = authenticate(username=usuario, password = contra)
                  
                  
                  if user is not None:
                        login(request, user)
                        avatares = Avatar.objects.filter(user=request.user.id).exists()
                        if avatares == True:
                              avatares = Avatar.objects.filter(user=request.user.id)
                              print(avatares)
                              return render(request, "app1/inicio.html", {"url": avatares[0].imagen.url})
                        #return render(request, "app1/inicio.html", {"mensaje": f"Bienvenido {usuario}"})
                        else:
                              return render(request, "app1/inicio.html", {"mensaje": f"Bienvenido {usuario}"})
                  else:
                        return render(request, "app1/error.html", {"mensaje": f"Error, datos incorrectos"})
            
            else:
                  return render(request,"app1/error.html", {"mensaje": f"Error, formulario equivocado"})      
      
      form = AuthenticationForm()
      return render(request, "app1/login.html", {"form": form})        
      
      
      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)
            
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')
                  
                  user = authenticate(username=usuario, password = contra)
                  
                  if user is not None:
                        login(request, user)
                        avatares = Avatar.objects.filter(user=request.user.id)
                        return render(request, "app1/inicio.html", {"url": avatares[0].imagen.url})
                        #return render(request, "app1/inicio.html", {"mensaje": f"Bienvenido {usuario}"})
                  else:
                        return render(request, "app1/error.html", {"mensaje": f"Error, datos incorrectos"})
            
            else:
                  return render(request,"app1/error.html", {"mensaje": f"Error, formulario equivocado"})      
      
      form = AuthenticationForm()
      return render(request, "app1/login.html", {"form": form})        

def register(request):
      
      
      form = UserRegisterForm(request.POST)
      if form.is_valid():
            
            username = form.cleaned_data['username']
            first_name=form.cleaned_data['first_name']
            
            form.save()
            return render(request, "app1/correcto.html", {"mensaje":"Usuario Creado!"})
      
      else:
            form = UserRegisterForm()
      
      return render(request, "app1/registro.html", {"form": form})      

@login_required
def editarPerfil(request):
      usuario = request.user
      
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST)
            if miFormulario.is_valid:
                  
                  informacion = miFormulario.data
                  
                  usuario.first_name = informacion['first_name']
                  usuario.email= informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password2']
                  usuario.save()
                  
                  return render (request, "app1/inicio.html")
      
      else:      
            
            miFormulario = UserEditForm(initial={ 'fist_name': usuario.first_name, 'email':usuario.email})
      
      return render(request, 'app1/editarPerfil.html', {'miFormulario':miFormulario, 'usuario':usuario})      

    
