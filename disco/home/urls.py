from django.urls import path

from .views import *

urlpatterns = [
    path("confirm-email/", ConfirmEmailView.as_view(), name="confirm-email"),
]
