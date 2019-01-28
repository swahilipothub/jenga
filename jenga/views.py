from django.shortcuts import render


def dashboard(request):
	dashboard = ""
	return render(request, 'dashboard.html', {'dashboard': dashboard})
