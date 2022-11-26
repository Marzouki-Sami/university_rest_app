from django.urls import include, path
from rest_framework import routers
from university_app import views


router = routers.DefaultRouter()
router.register(r'students', views.StudentViewSet)
router.register(r'groupes', views.GroupeViewSet)
router.register(r'teachers', views.TeacherViewSet)
router.register(r'modules', views.ModuleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('students/getbyid/<int:student_id>', views.update_or_delete_or_retrieve_student, name='retrieve_student'),
    path('students/save', views.retrieve_or_add_student, name='save_student'),
    path('students/getall', views.retrieve_or_add_student, name='get_all_students'),
    path('students/update/<int:student_id>', views.update_or_delete_or_retrieve_student, name='update_student'),
    path('students/delete/<int:student_id>', views.update_or_delete_or_retrieve_student, name='delete_student'),
    path('groupes/delete/<int:groupe_id>', views.update_or_delete_or_retrieve_groupe, name='delete_groupe'),
]
