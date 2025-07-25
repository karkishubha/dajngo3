from django.shortcuts import render

# Create your views here.
def home(request):
    display = ["Shubha","Roshan","Utkarsh","Anuj","Prashant"]
    return render(request, 'display_tmp/home.html',{'display_info':display})
