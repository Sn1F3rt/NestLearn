from django.urls import reverse_lazy
from django.views import generic

from . import forms


class Register(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/register.html"
