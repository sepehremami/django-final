from django import forms
from django.contrib.auth import get_user_model


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    email = forms.EmailField(
        required=True, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    phone = forms.EmailField(
        required=True, widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "phone_number"]


class UserAdminForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = "__all__"
