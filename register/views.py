from django.shortcuts import render, redirect
from .form import RegisterForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
        return redirect("/..")
    else:
        form = RegisterForm()
    return render(request, "register/register.html", {"form": form})


def loginError(request):
    return render(request, "register/loginerror.html")
