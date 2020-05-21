from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import requests
from django.urls import reverse

from .models import Comment, UserCommentRating


# @login_required
def index(request):
    pass
    return render(request, 'charityfinder_app/index.html')


def project_detail_view(request, pid):
    # refine
    url = f"https://api.globalgiving.org/api/public/projectservice/projects/{pid}.json?api_key=79638b32-7812-44ef-b361-9eb4ef85aae0"
    gg_api_res = requests.get(url)
    gg_api_data = gg_api_res.json()
    # print(data)
    comments = Comment.objects.filter(project_id=pid)  # .order_by('-rated', '-created')

    context = {
        'gg_api_data': gg_api_data,
        'pid': pid,
        'comments': comments,
    }
    return render(request, 'charityfinder_app/project.html', context)


def new_comment_view(request, pid):
    if request.method == 'POST' and request.user.is_authenticated:
        text = request.POST['newComment']
        comment = Comment()
        comment.body = text
        comment.author = request.user
        comment.project_id = pid
        if "reply" in request.POST:
            comment.parent = Comment.objects.get(pk=request.POST['reply'])
        comment.save()
        print('comment saved')
        # prevents previous post request on page reload
        return redirect(reverse('charityfinder_app:project', args={pid}))
    elif request.method == 'POST':
        print('not authorized to comment')


"""    if request.method == 'POST' and request.user.is_authenticated and request.POST['comment_rating']:
        state = request.POST['comment_rating']
        rated = UserCommentRating.objects.get_or_create(user=request.user, comment=pk selector)
        rated.state = state
        rated.save() """