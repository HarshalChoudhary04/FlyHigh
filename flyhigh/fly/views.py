from django.shortcuts import redirect, render
from fly.models import ConfirmBooking,Roots
from fly.forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate ,login ,logout
# Create your views here.
def home(request):
    
    return render(request,'fly/home.html')
def about(request):
    return render(request,'fly/about.html')
def services(request):
    return render(request,'fly/services.html')
def contact(request):
    return render(request,'fly/contact.html')
def loginPage(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            logfm = AuthenticationForm(request=request, data=request.POST)
            if logfm.is_valid():
                uname = logfm.cleaned_data['username']
                upass = logfm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    return redirect('/')                
        else:
            logfm = AuthenticationForm()
        return render(request,'fly/login.html',{'logfm':logfm})
    else:
        return redirect('/')

def logoutpage(request):
    logout(request)
    return redirect('/login/')

def registration(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            rgform = RegistrationForm(request.POST)
            if rgform.is_valid():
                rgform.save()
                return redirect('/login/')
        else:
            rgform = RegistrationForm()
        return render(request,'fly/registration.html',{'rgform':rgform})
    else:
        return redirect('/')        
def mybooking(request):
    books= ConfirmBooking.objects.filter(bookUser=request.user)
    return render(request,'fly/mybooking.html',{'books':books})
    
def selectflight(request):
    if request.method == 'POST':
        dep = request.POST['depart']
        arr = request.POST['arrival']
        clss = request.POST['class']
        global dt
        global ps
        dt= request.POST['date']
        ps = request.POST['passengers']
        if clss == "":
            root = Roots.objects.filter(dep_airport=dep,arr_airport=arr)
        else:
            root = Roots.objects.filter(dep_airport=dep,arr_airport=arr,cls=clss)
        return render(request,'fly/selectflight.html',{'root':root})
    else:
        return redirect('/')

def confirmbooking(request):
    if request.method =='POST':
        rtid = request.POST['rootid']
        book = Roots.objects.get(id=rtid)
        global root_info
        root_info = book
        return render(request,'fly/confirmbooking.html',{'booking':book,'jdate':dt,'pass':ps})
    else:
        return redirect('/')

def bookticket(request):
    if request.method == 'POST':
        root = request.POST['rootdet']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        address = request.POST['address']
        vaccine = request.POST['vaccinestaus']
        gender = request.POST['gender']
        totalfare = request.POST['totalamount']
        book= ConfirmBooking(
            bookUser = request.user,
            journey_details = root_info,
            journey_date = date,
            name= name,
            email=email,
            phone=phone,
            address=address,
            vaccine=vaccine,
            gender=gender,
            passenger=ps,
            totalfare=totalfare[4:]
        )
        book.save()
        return redirect('mybooking/')
    else:
        return redirect('/')