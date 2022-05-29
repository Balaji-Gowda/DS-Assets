from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import redirect, render

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "invalid credntials")
            return redirect("login")

    else:
        return render(request, "login.html")


def register(request):
    if request.method == "POST":
        fn = request.POST['fname']
        ln = request.POST['lname']
        un = request.POST['username']
        p1 = request.POST['p1']
        p2 = request.POST['p2']
        email = request.POST['email']

        if p1 == p2:
            if User.objects.filter(username=un).exists():
                messages.info(request, 'username taken already')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=un, first_name=fn, last_name=ln, email=email, password=p1)
                user.save()
                messages.info(request, 'user created')
                return redirect('login')
        else:
            messages.info(request, 'password not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
