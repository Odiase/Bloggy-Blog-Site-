from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseForbidden, HttpResponseNotFound

from .models import Blog, Comment
from .forms import BlogForm


# Create your views here.

def search_blogs(request):
    def add_to_all_blogs(list):
        for i in list:
            if i in all_blogs_result:
                pass
            else:
                all_blogs_result.append(i)
    
    all_blogs_result = []
    search_input = ""

    if request.method == "GET":
        search_input = request.GET.get("search-input")
        if search_input is not None:
            blogs_by_title = Blog.objects.filter(title__icontains = search_input)
            blogs_by_category = Blog.objects.filter(category__icontains = search_input)
            blogs_by_last_name = Blog.objects.filter(user__last_name__icontains = search_input)
            blogs_by_first_name = Blog.objects.filter(user__first_name__icontains = search_input)
            blogs_by_username = Blog.objects.filter(user__username__icontains = search_input)

            add_to_all_blogs(blogs_by_category)
            add_to_all_blogs(blogs_by_title)
            add_to_all_blogs(blogs_by_last_name)
            add_to_all_blogs(blogs_by_first_name)
            add_to_all_blogs(blogs_by_username)
        else:
            search_input = ""

    paginator = Paginator(all_blogs_result,100)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        "blogs":all_blogs_result,
        "search":search_input,
        "nob":len(all_blogs_result),
        "page":page_obj
    }

    return render(request,"blogs/search.html",context)


@login_required(login_url="login")
def create_blog(request):
    form = BlogForm()
    if request.method == "POST":
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            dummy = form.save(commit = False)
            dummy.user = request.user
            dummy.save()
            return redirect("single-blog",dummy.slug,dummy.id)
    context = {"form":form}
    return render(request,"blogs/create-blog.html",context)


def single_blog(request,slug,id):
    try:
        blog = Blog.objects.get(id = id)
    except:
        return HttpResponseNotFound()

    if request.method == "POST":
        if request.user.is_authenticated:
            comment = request.POST["comment"]
            comment_instance = Comment.objects.create(blog = blog, user = request.user,message = comment)
            comment_instance.save()
            return redirect("single-blog",blog.slug,blog.id)
        else:
            return redirect("login")
        
    related_blogs_objects = Blog.objects.filter(category = blog.category)[0:3]
    recent_blogs_objects = Blog.objects.all()[0:3]
    related_blogs = []
    recent_blogs = []
    for i in related_blogs_objects:
        if i == blog:
            pass
        else:
            related_blogs.append(i)
        
    for i in recent_blogs_objects:
        if i == blog:
            pass
        else:
            recent_blogs.append(i)

    recent_blogs_objects = Blog.objects.all()[0:3]

    context = {
        "blog":blog,
        "loc":len(blog.blog_comments),
        "comments":blog.blog_comments[0:3],
        "related_blogs":related_blogs,
        "recent_blogs":recent_blogs,
        "lor":len(related_blogs),
    }
    return render(request,"blogs/single-blog.html",context)


@login_required(login_url="login")
def update_blog(request,id):
    try:
        blog = Blog.objects.get(id = id)
    except:
        return HttpResponseNotFound()
    if blog.user != request.user:
        return HttpResponseForbidden()

    form = BlogForm(instance= blog)
    if request.method == "POST":
        form = BlogForm(request.POST,request.FILES,instance = blog)
        if form.is_valid():
            form.save()
            return redirect("single-blog", blog.slug, blog.id)
    context = {"form":form}
    return render(request,"blogs/update-blog.html",context)


@login_required(login_url = "login")
def delete_blog(request,id):
    try:
        blog = Blog.objects.get(id = id)
    except:
        return HttpResponseNotFound()
    if blog.user != request.user:
        return HttpResponseForbidden()

    if request.method == "POST":
        blog.delete()
        return redirect("home")
    context = {"blog":blog}
    return render(request,"blogs/delete-blog.html",context)