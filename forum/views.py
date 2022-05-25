from django.shortcuts import render
from forum.models import Post, Answer
from forum.forms import Post_form,Answer_form
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import space
from space.models import Space

@login_required
def list_forum(request,space_id):
    space = Space.objects.get(id = space_id)
    posts = Post.objects.filter(space = space).order_by('published_date')
    context = {"posts" : posts}
    return render(request, template_name="forum/forum_page.html" , context = context)

@login_required
def post_answer(request,space_id,post_id):
    space = Space.objects.get(id = space_id)
    post = Post.objects.get( id = post_id)
    answer = Answer.objects.filter(post = post).order_by("published_date")
    form = Answer_form()
    context = {
        "space" : space,
        "post"  : post,
        "answer": answer,
        "form"  : form,
    }
    return render(request,'forum/post_detail.html', context = context)

@login_required
def post_forum(request, space_id):
    space = Space.objects.get(id = space_id)
    if request.method == "POST":
        form = Post_form(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.space = space
            post.save()
            return render(request, "forum/forum_page.html")
    else:
        form = Post_form()
    return render(request,'forum/create_post.html',{"form":form , "space" : space})

@login_required
def post_detail(request,space_id,post_id):
    space = Space.objects.get(id = space_id)
    post = Post.objects.get( id = post_id)
    if request.method == "POST":
        form = Answer_form(data=request.POST)
        if form.is_valid():
            form.save()
            answers = Answer.objects.filter(post = post).order_by("published_date")
            return render(request, "forum/post_detail.html",{"form":form , "space" : space , "post" : post ,"answers" : answers})
    else:
        form = Answer_form()
        answers = Answer.objects.filter(post = post).order_by("published_date")
    return render(request, "forum/post_detail.html",{"form":form , "space" : space , "post" : post ,"answers" : answers})
