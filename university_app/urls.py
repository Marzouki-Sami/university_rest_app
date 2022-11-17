from django.urls import include, path
from rest_framework import routers
from university_app import views


router = routers.DefaultRouter()
router.register(r'students', views.StudentViewSet)
router.register(r'groupes', views.GroupeViewSet)
router.register(r'teachers', views.TeacherViewSet)
router.register(r'modules', views.ModuleViewSet)
router.register(r'sessions', views.SessionViewSet)


urlpatterns = [
    path('', include(router.urls))
]
