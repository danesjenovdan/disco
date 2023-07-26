from django.urls import path

from .views import *

urlpatterns = [
    path("confirm-email/", ConfirmEmailView.as_view(), name="confirm-email"),
    path("register/", RegistrationView.as_view(), name="registration"),
    path("thank-you/", RegistrationSuccessfulView.as_view(), name="thank-you-for-registration"),
    path("call-for-speakers/", ApplySpeakerView.as_view(), name="apply-to-be-a-speaker"),
    path("thank-you-for-application/", SpeakerApplicationSuccessfulView.as_view(), name="thank-you-speaker"),
]
