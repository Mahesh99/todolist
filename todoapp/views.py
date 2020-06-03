from django.shortcuts import render, redirect,HttpResponse
from django.views.generic import ListView
from .models import Todo

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
