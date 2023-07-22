from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm
from .models import User


def register_user(request):
    if request.method == "POST":
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            # Creating user using the form
            # password = form.cleaned_data["password"]
            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # user.save()

            # Creating user using create_user method
            del form.cleaned_data["confirm_password"]
            user = User.objects.create_user(**form.cleaned_data)
            user.role = User.CUSTOMER
            user.save()
            print("User is created")
            return redirect("register_user")

    else:
        form = UserForm()
        context = {
            "form": form,
        }
        return render(request, "accounts/register_user.html", context)
