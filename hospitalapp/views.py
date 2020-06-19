from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from hospitalapp.models import Departments, Doctors, Index, IndexDoctor, News, Patient, Popular, Appointment


# Create your views here.
def index(request):
    home = Index.objects.all()
    home1 = IndexDoctor.objects.all()
    new = News.objects.all()
    patient1 = Patient.objects.all()
    popular1 = Popular.objects.all()

    return render(request, 'index.html',
                  {'home': home, 'home1': home1, 'new': new, 'patient1': patient1, 'popular1': popular1})


def departments(request):
    department = Departments.objects.all()
    home = Index.objects.all()
    return render(request, 'departments.html', {'department': department, 'home': home})


def doctors(request):
    doctor = Doctors.objects.all()
    return render(request, 'doctors.html', {'doctor': doctor})


def blog_home(request):
    return render(request, 'blog-home.html')


def contact(request):
    return render(request, 'contact.html')


def aboutus(request):
    patient1 = Patient.objects.all()
    return render(request, 'about.html', {'patient1': patient1})


def blog_details(request):
    return render(request, 'blog-details.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        number = request.POST['number']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already Taken')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save();
                print('User Created')
        else:
            print('password not matching..')
        return redirect('index/')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('index/')


def login1(request):
    return render(request, 'login.html')


def register1(request):
    return render(request, 'register.html')


def appointment(request):
    if request.method == 'POST':
        username = request.POST['username']
        department = request.POST['department']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        message = request.POST['message']
        appoint = Appointment(username=username, department=department, email=email, phone=phone,  date=date,
                              message=message)
        appoint.save()

    return render(request, 'appointment.html')
