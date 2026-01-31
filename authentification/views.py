from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages

import datetime

def index(request):
	context={
	"message":"Hello word !!",
	"numberNews":9,
	"usersList":["Papa","Olivier","BAKOU","Fernand"],
	"publication":datetime.datetime.now(),
	"username":"BAKOU LONGO Olivier Fernand"
	}
	template=loader.get_template("authentification/login.html")
	return HttpResponse(template.render(context,request))

def login_view(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "Connexion réussie")
            return redirect("home")
        else:
            messages.error(request, "Identifiants incorrects")

    return render(request, "authentification/login.html")
