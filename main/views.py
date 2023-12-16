import json
from collections import defaultdict

from django.contrib import messages
from django.contrib.auth import authenticate
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

import main.get_info as Info
import main.models as models


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
        if found_user is not None:
            print(Info.get_student(email))
            return render(request, 'main/Personal.html', {'Info': Info.get_student(email)})
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


def journal_view(request, group_id, subject_id):
    students = models.User.objects.filter(group_id=group_id)
    markcells = models.MarkCell.objects.filter(subject_id=subject_id)
    student_progress = models.Progress.objects.filter(student__group_id=group_id,
                                                      subject_id=subject_id)
    student_progress_dict = defaultdict(dict)
    for progress in student_progress:
        student_progress_dict[progress.markcell_id][progress.student_id] = progress.mark

    return render(request, 'main/Journal.html', {'students': students, 'markcells': markcells,
                                                 'student_progress': student_progress,
                                                 'student_progress_dict': student_progress_dict,
                                                 'subject_id': subject_id})


def create_markcell(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        subject_id = request.POST.get('subject_id')
        new_markcell = models.MarkCell.objects.create(date=date, subject_id=subject_id)

        return JsonResponse({'message': 'Новый MarkCell успешно создан.'})
    return JsonResponse({'message': 'Ошибка: Метод не разрешен.'}, status=405)


def update_grade(request):
    if request.method == 'POST':
        progress_id = int(request.POST.get('progress_id')) if request.POST.get(
            'progress_id') else None
        new_grade = request.POST.get('new_grade')
        markcell_id = int(request.POST.get('markcell_id'))
        student_id = int(request.POST.get('student_id'))
        subject_id = int(request.POST.get('subject_id'))

        progress, created = models.Progress.objects.get_or_create(
            id=progress_id,
            defaults={'mark': new_grade,
                      "comment": "practice",
                      "student_id": student_id,
                      "markcell_id": markcell_id,
                      "subject_id": subject_id}
        )

        if not created:
            progress.mark = new_grade
            progress.comment = "practice"
            progress.save()

        return JsonResponse({'message': 'Новый MarkCell успешно создан.'})
    return JsonResponse({'message': 'Ошибка: Метод не разрешен.'}, status=405)


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
        if not first_name:
            return HttpResponse('First name cannot be empty')

        last_name = data.get('last_name')
        if not last_name:
            return HttpResponse('Last name cannot be empty')

        middle_name = data.get('middle_name')
        if not middle_name:
            return HttpResponse('Middle name cannot be empty')

        email = data.get('email')
        if not email:
            return HttpResponse('Email cannot be empty')

        age = data.get('age')
        if not age:
            return HttpResponse('Age cannot be empty')

        password = data.get('password')
        if not password:
            return HttpResponse('Password cannot be empty')

        role = data.get('role')
        if not role:
            return HttpResponse('Role cannot be empty')

        new_user = models.User(
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            age=age,
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
