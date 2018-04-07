from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, Http404,JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from .models import *
# Create your views here.

def index(request):
	response = {}
	return render(request, 'share/index.djt', response)

def signup(request):
    if request.user.is_active == True and request.user.is_authenticated():
        return redirect('/')
    if request.method == 'POST':
        if Userprofile.objects.filter(regNum=request.POST['regNum']).count() > 0 :
            response = {}
            response['error'] = 'This Registration Number Has Already Been Registered'
            return render(request, 'share/signup.djt', response)

        post_keys = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
        for i in post_keys:
            if(request.POST[i] == None or request.POST[i] == '') :
                return render('share/signup.djt', {'error' : "Data Error, Please Try Again."})
        username  = request.POST['username'].lower()
        emailadr  = request.POST['email']
        password  = request.POST['password1']
        password2 = request.POST['password2']
        first_name = request.POST['first_name']
        last_name  = request.POST['last_name']
        if password != password2 :
            return render(request, 'share/signup.djt', {'error' : 'Passwords don\'t match'})
        try:
            user = User._default_manager.get(username__iexact = username.lower())
            return render(request, 'share/signup.djt', {'error':'User-Name Already Exists'})
        except User.DoesNotExist:
            user = User.objects.create_user(username = username, email = emailadr, first_name = first_name, last_name = last_name)
            user.set_password(password)
            user.save()
            profile = Userprofile()
            profile.user = user
            profile.regNum = request.POST['regNum']
            profile.save()
            user = authenticate(username = username, password = password)
            login(request, user)
            
            return redirect('/updateProfile')
        # return redirect('/auth/login')
        
    return render(request, 'share/signup.djt', None)

def signin(request):
    if request.user.is_authenticated() and request.user.is_active == True :
        return redirect('/')
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = user_name, password = password)
        if user == None :
            return render(request, 'share/login.djt', {'error' : 'User-Name/Password Invalid'})
        elif user.is_active == False :
            login(request, user)
            return redirect('/auth/updateProfile')
        else : 
            login(request, user)
            return redirect('/')
    return render(request, 'share/login.djt')

def signout(request):
    logout(request)
    return redirect('/login')
    
def updateProfile(request) :
    response = {}
    if request.method == 'POST' :
        profile = Userprofile.objects.get(user=request.user)
        profile.course = request.POST['course']
        profile.branch = request.POST['branch']
        profile.contact = request.POST['contact']
        profile.year = request.POST['year']
        
        profile.save()

        return redirect('/profile/'+profile.regNum)
    return render(request,'share/updateProfile.djt',response)

def profile(request,regNum) :
    userProfile = Userprofile.objects.get(regNum=regNum)
    items = Item.objects.filter(owner=userProfile.user)
    response = {}
    response['userProfile'] = userProfile
    response['items'] = items
    return render(request,'share/profilepage.djt',response)

def manage(request):
    return redirect('/')

