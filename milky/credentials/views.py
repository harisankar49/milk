from django.shortcuts import render

# Create your views here.
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            print("invalid credentials")
            return redirect('login')
    return render(request, 'login.html')


def register(request):
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already exist")
                return redirect('register')


            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already registered')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save()

                messages.info(request, 'user created')

                print("User created")
                return redirect('login')
        else:

            messages.info(request, "password mismatches")
            print("password mismatches")
            return redirect('register')
    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    print("You are logged out")
    return redirect('/')


