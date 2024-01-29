from django.shortcuts import render


# Create your views here.


#----------------------------
def logIn(request):

	context = {
		'title': 'login',
	}
	return render(request, 'materiales_app/login.html', context)

#----------------------------

def list(request):

	context = {
		'title': 'Listado',
	}
	return render(request, 'materiales_app/list.html', context)

