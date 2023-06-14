from django.views.generic import TemplateView


class ConfirmEmailView(TemplateView):
    template_name = "home/confirm_email_view.html"
