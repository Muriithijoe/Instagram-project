from django.shortcuts import render

@login_required(login_url='/accounts/login/')
def post(request,post_id):
    try:
        post = Post.objects.get(id = post_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"post.html", {"post":post})
