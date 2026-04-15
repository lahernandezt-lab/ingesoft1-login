from django.urls import path
from auth_app.controllers.auth_controller import login

urlpatterns = [
    path('login', login),
]
