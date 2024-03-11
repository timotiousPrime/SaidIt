import http
from sys import prefix
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.forms import formset_factory

# Transaction
from django.db import transaction

# Generic Views
from django.views.generic import (
    View,
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

# Forms
from .forms import UserAccountForm, UserProfileForm, EmploymentHistoryForm

# Models
from django.contrib.auth.models import User
from .models import Employment_History, User_Profile

# Create your views here.


class LoginView(View):
    template_name = "/.html"


class LogoutView(View):
    template_name = "/.html"


class RegisterView(View):
    template_name = "/.html"


class AccountsListView(ListView):
    model = User
    template_name = "accounts/accountsListPage.html"


def accountCreateView(request):
    template_name = "accounts/accountCreatePage.html"
    EmploymentHistoryFormSet = formset_factory(EmploymentHistoryForm, extra=1)
    
    if request.method == "POST":
        user_form = UserAccountForm(request.POST, prefix="user_form")
        profile_form = UserProfileForm(request.POST, prefix="profile_form")
        employment_history_formset = EmploymentHistoryForm(request.POST, prefix="employment_history_formset")
        print(request.POST)
        
        if (user_form.is_valid() and profile_form.is_valid()):
            # Save user
            user_form.save()
            print("User saved!")
            # Create new profile instance, but dont save yet. First need to set the user
            profile_form.save(commit=False)
            print("Profile created")
            # Set the user for the profile
            profile_form.user.id = user_form.id
            print("profile updated with user")
            # save new profile instance
            profile_form.save()
            print("profile saved saved!")
            return HttpResponse("User and profile have been created and saved")



        return HttpResponse(request.POST)

    EmploymentHistoryFormSet = formset_factory(EmploymentHistoryForm, extra=1)
    employment_history_formset = EmploymentHistoryFormSet()
    user_form = UserAccountForm(prefix="user_form")
    profile_form = UserProfileForm(prefix="profile_form")
    employment_history_form = EmploymentHistoryForm()
    context = {
        "form": user_form,
        "profile_form": profile_form,
        "employment_history_formset": employment_history_formset,
    }

    return render(request, template_name, context)


class AccountCreateView(CreateView):
    template_name = "accounts/accountCreatePage.html"
    # model = User
    form_class = UserAccountForm
    success_url = reverse_lazy("account:Accounts")

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def form_valid(self, form):
        context = self.get_context_data()
        with transaction.atomic():
            # create new user
            print("new user")
        # save the user
        # # this will send a signal to create a profile
        # update profile with details from profile form
        # create new emp hist objects from form? iterate through form set, create new empHist

        # context = self.get_context_data()
        # user_profile_form = context["profile_form"]
        # user_profile_form = context["employment_history_form"]
        # # Use Django's transaction.atomic to ensure the atomicity of the operation
        # with transaction.atomic():
        #     response = super().form_valid(form)  # This will create the User

        #     # You can now access self.object to get the newly created User instance
        #     user = self.object

        #     # Creating the UserProfile
        #     profile_form_instance = UserProfileForm(self.request.POST)
        #     if profile_form_instance.is_valid():
        #         user_profile = profile_form_instance.save(commit=False)
        #         user_profile.user = user  # Set the foreign key to the new user
        #         user_profile.save()
        #     else:
        #         form.add_error(None, "User Profile data is invalid")
        #         return self.form_invalid(form)

        #     # Creating the EmploymentHistory
        #     employment_history_form_instance = EmploymentHistoryForm(self.request.POST)
        #     if employment_history_form_instance.is_valid():
        #         employment_history = employment_history_form_instance.save(commit=False)
        #         employment_history.user = user  # Set the foreign key to the new user
        #         employment_history.save()
        #     else:
        #         form.add_error(None, "Employment History data is invalid")
        #         return self.form_invalid(form)

        #     # Return the original response if all related objects are created successfully
        #     return response

    def get_context_data(self, **kwargs):
        # Add UserProfileForm and EmploymentHistoryForm to the context
        context = super().get_context_data(self, **kwargs)
        if self.request.POST:
            context["form"] = UserAccountForm(self.request.POST)
            context["profile_form"] = UserProfileForm(self.request.POST)
            context["employment_history_form"] = EmploymentHistoryForm(
                self.request.POST
            )
        else:
            context["form"] = UserAccountForm()
            context["profile_form"] = UserProfileForm()
            context["employment_history_form"] = EmploymentHistoryForm()
        return context


class AccountDetailView(DetailView):
    template_name = "accounts/accountDetailsPage.html"
    model = User


class AccountUpdateView(UpdateView):
    template_name = "accounts/accountUpdatePage.html"
    model = User


class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy("account:Accounts")
    template_name = "accounts/user_confirm_delete.html"
