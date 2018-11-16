from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import PostForm,ProfileForm,CommentForm
from .models import Post,Profile,Comment
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def post(request):
    try:
        posts = Post.objects.all()
    except DoesNotExist:
        raise Http404()
    return render(request,'post.html',{"posts":posts})

def profile(request):
    current_user = request.user
    post = Post.objects.filter(profile = current_user)

    try:
        # profile = get_object_or_404(Profile,user=current_user)
        profile = profile.objects.get(user=current_user)
    except ObjectDoesNotExist:
        return redirect('edit_profile.html')
    print(profile.bio)
    return render(request,'profile.html',{ 'profile':profile,'image':image,'current_user':current_user})

def photo(request,image_id):
    try:
        post = Post.objects.get(id = image_id)
    except ObjectDoesNotExist:
        return redirect('new_photo.html')
    return render(request,'photo.html',{'photo':photo})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit = False)
            image.profile = current_user
            image.save()
        return redirect('post')
    else:
        form =PostForm()
    return render(request,'new_post.html', {'form':form})

def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.profile = current_user
            profile.save()
        return redirect('profile')
    else:
        form = ProfileForm()
    return render(request,'edit_profile.html', {'form':form})

def search_results(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profile = Profile.search_by_username(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"profiles": searched_profile})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
# 
# def search_profile(request,profile_id):
#     try :
#         profile = profile.objects.get(id = profile_id)
#
#     except ObjectDoesNotExist:
#         # raise Http404()
#         return render(request, 'no_profile.html')
#
#     return render(request, 'search_profile.html', {'profile':profile})

def comment_photo(request, image_id):
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        image = get_object_or_404(Image, pk = image_id)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.comment = current_user
            comment.image = image
            comment.save()
        return redirect('comment-photo')
    else:
        form = CommentForm()
    return render(request,'comment.html', {'form':form})
