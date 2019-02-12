from django.shortcuts import render, redirect
from .forms import TodoModelForm
from django.contrib.auth.decorators import login_required
from .models import Todo
# Create your views here.
@login_required
def list(request):
    todos = request.user.todo_set.all()
    
    return render(request, "todo/list.html", {'todos':todos})

def detail(request,id):
    todo = Todo.objects.get(id=id)

    return render(request,"todo/detail.html",{"todo":todo})



#로그인 요청사항 추가!!!
@login_required
def create(request):
    if request.method == "POST":
        form = TodoModelForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todos:list')
    else:
        form = TodoModelForm()
    return render(request, "todo/create.html", {"form":form})
    
    
def update(request, id):
    todo = Todo.objects.get(id=id)
    
    if request.method == "POST":
        form = TodoModelForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            
            return redirect("todos:list")
    else:
        form = TodoModelForm(instance=todo)
    return render(request, 'todo/update.html', {'form':form})
        
