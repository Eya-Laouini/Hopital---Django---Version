from django.http import HttpResponse
from django.template import loader
from hopital.models import Patient
from hopital.models import Service
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def index(request):
    pat = Patient.objects.all().values()
    ser = Service.objects.all().values()
    template = loader.get_template('dashboard.html')
    context = {
    'pat': pat,
    'ser': ser,
    }
    return HttpResponse(template.render(context, request))

def del_pat(request,id):
    patient = Patient.objects.get(id=id)
    patient.delete()
    return HttpResponseRedirect(reverse('patients'))

def update_pat(request,id):
    pat = Patient.objects.get(id=id)
    ser = Service.objects.all().values()
    template = loader.get_template('updatePatient.html')
    context = {
    'pat': pat,
    'ser': ser,
    }
    return HttpResponse(template.render(context, request))

def list_ser(request):
    ser = Service.objects.all().values()
    template = loader.get_template('service.html')
    context = {
    'ser': ser,
    }
    return HttpResponse(template.render(context, request))

def del_ser(request,id):
    service = Service.objects.get(id=id)
    service.delete()
    return HttpResponseRedirect(reverse('services'))

def update_pat_action(request,id):
    nom = request.POST['nom']
    prenom = request.POST['prenom']
    numtel = request.POST['numtel']
    dateNais = request.POST['dateNais']
    service = request.POST['service']
    ser = Service.objects.get(id=service)
    patient = Patient.objects.get(id=id)
    patient.nom = nom
    patient.prenom = prenom
    patient.numtel = numtel
    patient.dateNais = dateNais
    patient.service = ser
    patient.save()
    return HttpResponseRedirect(reverse('patients'))

def add(request):
    ser = Service.objects.all().values()
    template = loader.get_template('addPatient.html')
    context = {
    'ser': ser,
    }
    return HttpResponse(template.render(context, request))
    
def addp(request):
    ser=Service.objects.all().values()
    template = loader.get_template('addPatient.html')
    context ={
        'ser':ser,
    }
    return HttpResponse(template.render(context, request))



def add_pat(request):
    pat = Patient()
    pat.nom = request.POST['nom']
    pat.prenom = request.POST['prenom']
    pat.numtel = request.POST['numtel']
    pat.dateNais = request.POST['dateNais']
    pat.service = Service.objects.get(id=request.POST['service'])
    pat.save()
    return HttpResponseRedirect(reverse('patients'))

def list_users(request):
    users = User.objects.all().values()
    template = loader.get_template('user.html')
    context = {
    'users': users,
    }
    return HttpResponse(template.render(context, request))

def del_user(request,id):
    user = User.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse('user'))

def create_compte(request):
    user_form = FormUser()
    return render(request, 'createUser.html', {'user_form': user_form})

def create_user_action(request):
   addEmail = request.POST['email']
   username = request.POST['login']
   password = request.POST['mot2pass']
   confirm  = request.POST['confirm']
   nom = request.POST['nom']
   if (password == confirm):
       user = User.objects.create_user(username, addEmail, password)
       user.first_name = nom
       user.save()
       return HttpResponseRedirect(reverse('user'))

def connexion(request):
    connexion_form = UserConnectForm()
    return render(request, 'connexion.html', {'connexion_form': connexion_form, 'error': False})

def signIn(request):
    username = request.POST['login']
    password = request.POST['mot2pass']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        request.session['username'] = username
        return HttpResponseRedirect(reverse('patients'))
    else:
        print('Login et/ou mot de passe incorrect')
        return render(request, 'connexion.html', {'error': True})

def signOut(request):
    logout(request)
    return HttpResponseRedirect(reverse('connexion'))

def update_user(request,id):
    user = User.objects.get(id=id)
    template = loader.get_template('updatUser.html')
    context = {
    'user': user,
    }
    return HttpResponse(template.render(context, request))

def update_user_action(request,id):
    nom = request.POST['nom']
    prenom = request.POST['prenom']
    numtel = request.POST['numtel']
    dateNais = request.POST['dateNais']
    service = request.POST['service']
    ser = Service.objects.get(id=service)
    ser = Patient.objects.get(id=id)
    ser.nom = nom
    ser.prenom = prenom
    ser.numtel = numtel
    ser.dateNais = dateNais
    ser.service = ser
    ser.save()
    return HttpResponseRedirect(reverse('patients'))

def update_user(request,id):
    user = User.objects.get(id=id)
    template = loader.get_template('updateUser2.html')
    context = {
    'user': user,
    }
    return HttpResponse(template.render(context, request))

def update_user_action(request,id):
    user = User.objects.get(id=id)
    user.last_name = request.POST['last_name']
    user.first_name = request.POST['first_name']
    user.email = request.POST['email']
    user.username = request.POST['username']
    user.password = request.POST['newPassword']
    user.password = request.POST['confirmPassword']
    user.save()
    return HttpResponseRedirect(reverse('user'))










