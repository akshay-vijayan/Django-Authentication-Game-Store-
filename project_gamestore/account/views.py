from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,FormView,CreateView
from .forms import LoginForm,RegForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages


# Create your views here.

class LoginPageView(FormView):
    template_name='login.html'
    form_class=LoginForm

    def post(self,request):
        form_data=LoginForm(data=request.POST)
        if form_data.is_valid():
            nuser=form_data.cleaned_data.get("username")
            pswd=form_data.cleaned_data.get("password")      
            user=authenticate(request,username=nuser,password=pswd)
            if user:
                messages.success(request,"the user successfully logged in")
                return redirect('home')
            else:
                messages.error(request,"login failed")
                return redirect('login')
        else:
            return render(request,'login.html',{"form":form_data})
        
class RegView(CreateView):
    template_name='reg.html'
    form_class=RegForm
    success_url=reverse_lazy('login')




