from django.urls import path, include
from . import views  # Correct import for views
from django.contrib import admin  # Import Django's built-in admin site

from .views import upload_file

urlpatterns = [
    path('',views.projecthomepage, name = 'projecthomepage'),
    path('printpagecall/',views.printpagecall, name = 'printpagecall'),
    path('printpagelogic/',views.printpagelogic, name = 'printpagelogic'),
    path('exceptionpagecall/',views.exceptionpagecall, name = 'exceptionpagecall'),
    path('exceptionpagelogic/',views.exceptionpagelogic, name = 'exceptionpagelogic'),
    path('UserRegisterCall/',views.UserRegisterCall, name = 'UserRegisterCall'),
    path('UserRegisterLogic/', views.UserRegisterLogic, name='UserRegisterLogic'),
    path('UserLoginPageCall/', views.UserLoginPageCall, name='UserLoginPageCall'),
    path('UserLoginLogic/', views.UserLoginLogic, name='UserLoginLogic'),
    path('logout/', views.logout, name='logout'),
    # path('admin/', admin.site.urls),
    # path('faculty/', include('facultyapp.urls')),  # Include faculty app URLs
    path('add_student/', views.add_student, name='add_student'),
    path('studentlist/', views.studentlist, name='studentlist'),

    path('add_task/', views.add_task, name='add_task'),
    path('<int:pk>/delete/', views.delete_task, name='delete_task'),

    path('datetimepagelogic/', views.datetimepagelogic, name='datetimepagelogic'),
    path('datetimepagecall/', views.datetimepagecall, name='datetimepagecall'),
    path('otppagelogic/', views.otppagelogic, name='otppagelogic'),
    path('otppagecall/', views.otppagecall, name='otppagecall'),
    path('feedback_view/', views.feedback_view, name='feedback_view'),
    path('calculatorlogic/', views.calculatorlogic, name='calculatorlogic'),
    path('upload/', upload_file, name='upload_file'),
    path('conmanager/', views.conmanager, name='contact_manager'),
    path('<int:pk>/delete_manager/', views.delete_manager, name='delete_manager'),

]