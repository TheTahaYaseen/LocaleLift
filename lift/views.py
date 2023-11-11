from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def home_view(request):
    context = {}
    return render(request, "lift/home.html", context)

def register_view(request):

    form = UserCreationForm()
    error = ""

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("home")
        else:
            error = form.errors.as_text()

    context = {"form": form, "error": error}
    return render(request, "lift/register.html", context)

def login_view(request):

    error = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username = username)
        except User.DoesNotExist:
            error = "User Does Not Exist!"

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("home")
        
        else:
            error = "An Error Occured During Login!"

    context = {"error": error}
    return render(request, "lift/login.html", context)