from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import UserAccount


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = UserAccount
        fields = ["email",  "first_name", "last_name"]
        error_class = "error"


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserAccount
        fields = ["email",  "first_name", "last_name"]
        error_class = "error"
