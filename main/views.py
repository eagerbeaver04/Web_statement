from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
import main.models as models
from django.views.decorators.csrf import csrf_exempt
import json


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
        found_user = authenticate(request, login=email, password=password)
        print(found_user.serialize())
        if found_user is not None:
            return render(request, 'main/Personal.html', found_user.serialize())
        else:
            messages.error(request, "Invalid login credentials")
            return redirect('sign')


def createuser(request):
    user = models.User(
        first_name=request.POST.get("first_name", "Undefined"),
        last_name=request.POST.get("last_name", "Undefined"),
        middle_name=request.POST.get("middle_name", "Undefined"),
        email=request.POST.get("email", "Undefined"),
        password=request.POST.get("password", "Undefined"),
        gender=request.POST.get("gender", "Undefined"),
        age=request.POST.get("age", "Undefined"),
        role=request.POST.get("role", "Undefined"),
    )
    user.save()
    return JsonResponse(user.serialize())


@csrf_exempt
def user(request):
    if request.method == 'GET':
        email = request.GET['email']
        found_user = models.User.objects.get(email=email)
        serialized_user = found_user.serialize()
        return JsonResponse(serialized_user)
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        first_name = data.get('first_name')
        print(data)
        if not first_name:
            return HttpResponse('First name cannot be empty')

        last_name = data.get('last_name')
        if not last_name:
            return HttpResponse('Last name cannot be empty')

        email = data.get('email')
        if not email:
            return HttpResponse('Email cannot be empty')

        password = data.get('password')
        if not password:
            return HttpResponse('Password cannot be empty')

        role = data.get('role')
        if not role:
            return HttpResponse('Role cannot be empty')

        new_user = models.User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            role=role,
        )
        new_user.save()
        return HttpResponse('Successful')
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass


@csrf_exempt
def get_student_subjects(request):
    if request.method != 'GET':
        return HttpResponse('Forbidden')

    email = request.GET['email']
    found_user = models.User.objects.get(email=email)

    if found_user.role != models.User.Roles.STUDENT:
        return HttpResponse('Forbidden')

    group = found_user.group
    subjects = group.subjects.all()
    response = []
    for subject in subjects:
        response.append(subject.serialize())

    return JsonResponse(response, safe=False)


@csrf_exempt
def get_professor_groups(request):
    if request.method != 'GET':
        return HttpResponse('Forbidden')

    email = request.GET['email']
    found_user = models.User.objects.get(email=email)

    if found_user.role != models.User.Roles.PROFESSOR:
        return HttpResponse('Forbidden')

    subjects = found_user.subjects.all()
    response = []
    for subject in subjects:
        subject_groups = subject.groups.all()
        for group in subject_groups:
            response.append(group.serialize())

    return JsonResponse(response, safe=False)
