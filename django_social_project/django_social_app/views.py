from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from .models import Blogs,Comments

def login(request):
    context = RequestContext(request, {
        'request': request, 'user': request.user,})
    return render_to_response('login.html', context_instance=context)


@login_required(login_url='/')
def home(request):
    return render_to_response('home.html')

def logout(request):
    auth_logout(request)
    return redirect('/')

@login_required(login_url='/')
def blogs(request):
    context = RequestContext(request, {
        'request': request, 'user': request.user,'email':request.user.email})
    print request.user.email
    
    if request.method == 'POST':
        blog=Blogs(
                email=request.user.email,
                title=request.POST['title'],
                text=request.POST['text'],
                )
        blog.save()
        
    return render_to_response('blogs.html', context_instance=context)


@login_required(login_url='/')
def getBlogs(request):
    context = RequestContext(request, {
                    'request': request, 
                    'user': request.user,
                    'email':request.user.email,
                    'blogs':Blogs.objects.filter(email=request.user.email)
                    })
    
    return render_to_response('listofblogs.html', context_instance=context)


@login_required(login_url='/')
def addcomments(request,bid):
    context = RequestContext(request, {
                    'request': request, 
                    'user': request.user,
                    'email':request.user.email,
                    'blogs':Blogs.objects.filter(email=request.user.email),
                    'comments':Comments.objects.filter(blog_id=bid)
                    })
    
    if request.method == 'POST':
        blog = Comments(
                blog_id=bid,
                comment=request.POST['comment'],
                )
        blog.save()
         
    return render_to_response('comment.html', context_instance=context)