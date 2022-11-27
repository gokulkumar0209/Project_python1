from django.shortcuts import render

# Create your views here.
def homepage_view(request):
	return render(request,"Product/html_files/Welcome.html")
def exit_view(request):
	return render(request,"Product/html_files/exit.html")
