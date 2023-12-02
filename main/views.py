from django.shortcuts import render


# Create your views here.
def main(request):
    return render(request, 'main/main.html')


def sign(request):
    return render(request, 'main/Sign.html')


def personal(request):
    return render(request, 'main/Personal.html')
