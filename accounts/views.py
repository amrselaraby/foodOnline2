from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm
from .models import User
from django.contrib import messages


def register_user(request):
    if request.method == "POST":
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
            messages.success(request, "Your account has been created successfully !.")
            return redirect("register_user")
        else:
            print("invalid form")
            print(form.errors)

    else:
        form = UserForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/register_user.html", context)


def register_vendor(request):
    context = {}
    return render(request, "accounts/register_vendor.html", context)
