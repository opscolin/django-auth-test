from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.



@login_required
def index(request):
	#return render(request, 'accounts/index.html')
	return render(request, 'accounts/index.html')

@login_required
def detail(request):
	#return render(request, 'accounts/detail.html')
	return render(request, 'accounts/detail.html')

def login(request):
	if request.method == 'GET':
		#return render(request, 'accounts/login.html')
		return render(request, 'accounts/login.html')
	else:
		username = request.POST.get('username')
		password = request.POST.get('password')
		print(username)
		print(password)
		user = auth.authenticate(username=username,password=password)
		print(user)
		if user is not None and user.is_active:
			auth.login(request, user)
			#return render(request, 'accounts/index.html')
			return render(request, 'accounts/index.html')
		else:
			print('user is invalid')
			#return render(request, 'accounts/login.html')
			return render(request, 'accounts/login.html')
	
				
@login_required
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect("/accounts/login")
