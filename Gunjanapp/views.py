from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection

def home(request):
    # return HttpResponse("<h1> Welcome to About page </h1>")
    cursor=connection.cursor()
    cursor.execute("select * from new_table where softdelete=0")
    columns = [col[0] for col in cursor.description]
    posts =  [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
    print(posts)
    context={
        'keypost':posts
    }
    # third parameter should always be a dictionary
    return render(request,'Gunjanapp/home.html',context)

def create(request):
    return render(request,'Gunjanapp/form.html')

def insert(request):
    title = request.POST['blogTitle']
    content = request.POST['content']
    cursor = connection.cursor()
    cursor.execute("INSERT INTO new_table (`title`,`content`) VALUES ( %s, %s );", (title, content))
    cursor = connection.cursor()
    cursor.execute("SELECT * from new_table")
    print(request)
    return redirect('/gunjanapp/home')

# Create your views here.

def edit(request,pk):
    print(pk)
    cursor=connection.cursor()
    cursor.execute("select * from new_table where softdelete=0 and id=%s",pk)
    columns = [col[0] for col in cursor.description]
    posts =  [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
    print(posts)
    context={
        'keypost':posts[0]
    }
    return render(request,'Gunjanapp/form2.html',context)


def update(request):
    title = request.POST['blogTitle']
    content = request.POST['content']
    id=request.POST['id']
    cursor = connection.cursor()
    cursor.execute("Update new_table set title=%s,content=%s where id=%s;", (title, content, id))
    cursor = connection.cursor()
    print(request)
    return redirect('/gunjanapp/home')


def delete(request,pk):
    print(pk)
    cursor = connection.cursor()
    cursor.execute("update new_table set softdelete=1 where id=%s",(pk,))
    cursor = connection.cursor()
    return redirect('/gunjanapp/home')




































    












    


