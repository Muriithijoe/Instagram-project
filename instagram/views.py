from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.shortcuts import render,redirect
from .forms import PostForm,ProfileForm,CommentForm
from .models import Post,profile
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def post(request):
    try:
        post = Post.objects.all()
    except DoesNotExist:
        raise Http404()
    return render(request,"post.html")
#
# @login_required(login_url='/accounts/login')
# def new_post(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.editor = current_user
#             post.save()
#         return redirect('NewsToday')
#     else:
#         form = PostForm()
#     return render(request, 'new_post.html', {"form": form})
#
#
# @login_required(login_url='/accounts/login/')
# def find(request, name):
#     results = profile.find_profile(name)
#     return render(request, 'search.html', locals())
#
# @login_required(login_url='/accounts/login/')
# def comment_on(request, post_id):
#     commentform = CommentForm()
#     post = get_object_or_404(Post, pk=post_id)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.user = request.user.profile
#             comment.photo = post
#             comment.save()
#     return render(request, 'post.html', locals())
