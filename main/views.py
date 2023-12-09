from django.http import HttpResponse
from django.shortcuts import render


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
    email = request.POST.get("email", "Undefined")
    password = request.POST.get("password", "Undefined")
    print(email)
    print(password)
    return HttpResponse(f"<h2>email: {email}  password: {password}</h2>")
