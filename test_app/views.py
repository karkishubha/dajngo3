from django.shortcuts import render

# Create your views here.
def home(request):
    profile = ["Shubha"]
    return render(request, 'test_temp/home.html',{'profile_info':profile})