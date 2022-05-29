from django.shortcuts import redirect, render
from forum.models import Post, Answer
from forum.forms import Post_form,Answer_form
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from space.models import Space

@login_required
def list_forum(request,space_id):
    space = Space.objects.get(id = space_id)
    posts = Post.objects.filter(space = space).order_by('published_date')
    context = {"posts" : posts , "space" : space}
    return render(request, template_name="forum/forum_page.html" , context = context)

@login_required
def post_answer(request,space_id,post_id):
    space = Space.objects.get(id = space_id)
    post = Post.objects.get( id = post_id)
    answer = Answer.objects.filter(post = post).order_by("published_date")
    answer_form = Answer_form()
    context = {
        "space" : space,
        "post"  : post,
        "answer": answer,
        "answer_form"  : answer_form,
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
            answers = Answer.objects.filter(post = post).order_by("published_date")
            answer_form = Answer_form(data=request.POST)
            return render(request, "forum/post_detail.html", {"space" : space , "post":post, "answers" : answers, "answer_form" : answer_form})
    else:
        form = Post_form()
    return render(request,'forum/create_post.html',{"form":form , "space" : space})

@login_required
def post_detail(request,space_id,post_id):
    space = Space.objects.get(id = space_id)
    post = Post.objects.get( id = post_id)
    if request.method == "POST":
        answer_form = Answer_form(data=request.POST)
        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.author = request.user
            answer.post = post
            answer.save()
            answers = Answer.objects.filter(post = post).order_by("published_date")
            return render(request, "forum/post_detail.html",{"answer_form":answer_form , "space" : space , "post" : post ,"answers" : answers})
    else:
        answer_form = Answer_form()
        answers = Answer.objects.filter(post = post).order_by("published_date")
    return render(request, "forum/post_detail.html",{"answer_form":answer_form , "space" : space , "post" : post ,"answers" : answers})
