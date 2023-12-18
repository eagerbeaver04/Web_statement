import main.models as models


def get_student(email):
    response = []
    found_user = models.User.objects.get(email=email)

    if found_user.role != models.User.Roles.STUDENT:
        return None

    response.append(found_user.serialize())

    group = found_user.group
    subjects = group.subjects.all()
    for subject in subjects:
        response.append(subject.serialize())

    progresses = models.Progress.objects.filter(student_id=found_user.id)
    for progress in progresses:
        response.append(progress.serialize())

    return response


def get_professor_groups(email):
    response = []
    found_user = models.User.objects.get(email=email)

    if found_user.role != models.User.Roles.PROFESSOR:
        return None

    subjects = found_user.subjects.all()
    response = []
    for subject in subjects:
        subject_groups = subject.groups.all()
        for group in subject_groups:
            response.append(group.serialize())

    return response


def get_professor_group_progress(email, group):
    response = []
    found_user = models.User.objects.get(email=email)

    if found_user.role != models.User.Roles.PROFESSOR:
        return None
