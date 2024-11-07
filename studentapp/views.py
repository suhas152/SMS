from django.shortcuts import render

def StudentHomePage(request):
    return render(request, "studentapp/StudentHomePage.html")


from django.contrib.auth.models import User
from django.shortcuts import render
from facultyapp.models import marks  # Ensure that this is the correct model name
from adminapp.models import StudentList


def view_marks(request):
    user = request.user


    
    try:
        student_user = User.objects.get(username=user.username)
        student = StudentList.objects.get(Register_Number=student_user)
        student_marks = marks.objects.filter(student=student)  # Use `marks` if it is lowercase

        return render(request, 'studentapp/marks.html', {
            'marks': student_marks  # Pass marks to the template
        })

    except (StudentList.DoesNotExist, User.DoesNotExist):
        return render(request, 'studentapp/error.html', {
            'error': 'No student found'
        })
