from django.shortcuts import render, redirect
from django.http import HttpResponse

from vendor.forms import VendorForm
from .forms import UserForm
from .models import User, UserProfile
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
    if request.method == "POST":
        # STORE THE DATA AND CREATE THE USER
        form = UserForm(request.POST)
        v_form = VendorForm(request.POST, request.FILES)
        if form.is_valid() and v_form.is_valid():
            # Creating user using create_user method
            del form.cleaned_data["confirm_password"]
            user = User.objects.create_user(**form.cleaned_data)
            user.role = User.VENDOR
            user.save()
            vendor = v_form.save(commit=False)
            vendor.user = user
            user_profile = UserProfile.objects.get(user=user)
            vendor.user_profile = user_profile
            vendor.save()
            messages.success(
                request,
                "Your account has been created successfully!, Please wait for the approval",
            )
            return redirect("register_vendor")
        else:
            print("invalid forms")
            print(form.errors)
            print(v_form.errors)
    else:
        form = UserForm()
        v_form = VendorForm()

    context = {
        "form": form,
        "v_form": v_form,
    }
    return render(request, "accounts/register_vendor.html", context)
