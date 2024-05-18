
from django.urls import path, include
from rest_framework.routers import DefaultRouter # type: ignore
from .views import AuthCheck,LoginView,expire_session_view,add_drone,control_drone,User_view
from . import views


router = DefaultRouter()
# router.register('drone', DroneListCreateAPIView, basename='drones')
# router.register(r'users',User_view, basename='user' )

urlpatterns = [
    path('auth_check/', AuthCheck.as_view(), name='auth_check'),
    path('login/', LoginView.as_view(),name='login'),
    path('expire-session/<str:session_key>/',expire_session_view, name='expire_session'),
    path('add_drone/',views.add_drone, name='add_drone'),
    path('control_drone/',views.control_drone, name='control_drone'),
    path('user/',User_view.as_view(),name='user'),
]
