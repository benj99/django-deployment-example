from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'temp_app/homepage.html')

def other(request):
    return render(request,'temp_app/other.html')

def relative(request):
    return render(request,'temp_app/relative_url_templates.html')
