from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext 
from timesheetapp.models import Timesheet
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm

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
            return HttpResponse("it worked!")
        else:
            #render_to_response('timesheetapp/register.html', {"The form is invalid":errormsg},context_instance=RequestContext(request))
			return HttpResponse("the bug is here")
    else:
        userform = UserCreationForm()
        return render_to_response('timesheetapp/register.html', {"userform":userform},context_instance=RequestContext(request))

def login(request):
    return render_to_response('timesheetapp/login.html')