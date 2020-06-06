from django.shortcuts import render, redirect,HttpResponse
from django.views.generic import ListView
from django.views import View
from .models import Todo
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages

class Home(ListView):
    model = Todo

    # def get(self,request,**kwargs):
    #     return HttpResponse("hello world")

    def post(self, request, **kwargs):
        # print(request.POST)
        content = request.POST.get('content')
        if content:
            todo = Todo.objects.create(content=content)
            todo.save()
        else:
            keys = request.POST.keys()
            for key in keys:
                if key != 'csrfmiddlewaretoken':
                    Todo.objects.get(id=int(key)).delete()
        return redirect('home')


class RegisterView(View):

    def get(self,request, **kwargs):
        form = UserRegistrationForm()
        return render(request, 'todoapp/register.html', {'form':form})
    
    def post(self, request, **kwargs):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            un = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            email = form.cleaned_data['email']
            if password1 == password2:
                user = User.objects.create_user(username=un, password=password1, email=email)
                user.save()
                messages.success(request, "Account created successfully")
        return redirect('register')