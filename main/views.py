from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login


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

        # Authenticate the user using the custom backend
        user = authenticate(request, login=email, password=password)

        if user is not None:
            # If authentication is successful, log the user in
            return render(request, 'main/Personal.html')
        else:
            # If authentication fails, render the login page with an error message
            error_message = "Invalid login credentials"
            return render(request, 'main/Sign.html', {'error_message': error_message})

