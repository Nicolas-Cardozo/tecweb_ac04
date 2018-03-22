from django.shortcuts import render
from django.http import HttpResponse


def index(request):
		return render(request, "index.html")
	
def login(request):
		if request.method == "GET":
			print("Acesso via POST")
		else:
			print("Acesso via GET")
		return render(request, "login.html")
		

		
		
		
		
		
		
