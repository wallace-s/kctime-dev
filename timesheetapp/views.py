from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext 
from timesheetapp.models import Timesheet
from django.contrib.auth import logout
from django.contrib.auth import login as django_login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

@login_required
def index(request):
    return render_to_response('timesheetapp/index.html', {}, context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/login/")
    
def register(request):
    if request.method == "POST":
        userform = UserCreationForm(request.POST)
        if userform.is_valid():
            userform.save()
            return HttpResponseRedirect("/success/")
        else:
            return render_to_response('timesheetapp/register.html', {"userform":userform, "errormsg":"Passwords didn't match. Try again."},context_instance=RequestContext(request))
    else:
        userform = UserCreationForm()
        return render_to_response('timesheetapp/register.html', {"userform":userform},context_instance=RequestContext(request))

# def login(request):
    # users = User.objects.all()
    # django_login(request)
    
    #return render_to_response('registration/login.html', {"users":users})
    
def sucess(request):
    return render_to_response('timesheetapp/success.html', {"user":request.user})