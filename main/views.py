from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.
def main(request):
    return render(request, 'main/main.html')


def sign(request):
    return render(request, 'main/Sign.html')


def personal(request):
    return render(request, 'main/Personal.html')


def reguser(request):
    first_name = request.POST.get("first_name", "Undefined")
    last_name = request.POST.get("last_name", "Undefined")
    email = request.POST.get("email", "Undefined")
    password = request.POST.get("password", "Undefined")


def enteruser(request):
    if request.method == 'POST':
        email = request.POST.get("email", "Undefined")
        password = request.POST.get("password", "Undefined")

        user = authenticate(request, login=email, password=password)
        if user is not None:
            return render(request, 'main/Personal.html', user.create_dict())
        else:
            messages.error(request, "Invalid login credentials")
            return redirect('sign')

