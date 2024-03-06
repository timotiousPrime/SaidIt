# Models
from django.contrib.auth.models import User
from .models import User_Profile, Employment_History

# Forms
from django.contrib.auth.forms import UserCreationForm
from django import forms

# Crispy forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class meta:
        model = User
        fields = ["username", "password1", "password2"]


class UserAccountForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

    def __ini__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = "form-horizontal"
        self.helper.add_input(Submit("submit", "Submit"))


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    surname = forms.CharField(required=True)
    email = forms.EmailField()

    class Meta:
        model = User_Profile
        fields = (
            "title",
            "first_name",
            "surname",
            "date_of_birth",
            "email",
            "phone_number",
            "interests",
        )
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
            "interests": forms.SelectMultiple(
                attrs={
                    "class": "form-select select2 interests-multiple",
                    "placeholder": "Select Interests",
                    "id": "InterestsSelect",
                }
            ),
        }

    def __ini__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = "form-horizontal"
        self.helper.add_input(Submit("submit", "Submit"))


class EmploymentHistoryForm(forms.ModelForm):
    class Meta:
        model = Employment_History
        fields = ("company", "position", "start_date", "end_date")
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
            "position": forms.SelectMultiple(
                attrs={
                    "class": "form-select select2 postion-multiple",
                    "placeholder": "Select postion",
                    "id": "PostionSelect",
                }
            ),
        }

    def __ini__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = "form-horizontal"
        self.helper.add_input(Submit("submit", "Submit"))
