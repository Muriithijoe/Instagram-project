from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def post(request):
    try:
        post = Post.objects.all()
    except DoesNotExist:
        raise Http404()
    return render(request,"post.html", {"post":post})

@login_required(login_url='/accounts/login')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.editor = current_user
            post.save()
        return redirect('NewsToday')
    else:
        form = PostForm()
    return render(request, 'new_post.html', {"form": form})


@login_required(login_url='/accounts/login/')
def find(request, name):
    results = Profile.find_profile(name)
    return render(request, 'search.html', locals())
