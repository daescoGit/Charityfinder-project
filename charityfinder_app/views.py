from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
import requests
from django.urls import reverse

from .models import Comment, UserCommentRating, UserProjectRating, project_calculated_rating


def index(request):
    pass
    return render(request, 'charityfinder_app/index.html')


def project_detail(request, pid):
    # refine
    url = f"https://api.globalgiving.org/api/public/projectservice/projects/{pid}.json?api_key=79638b32-7812-44ef-b361-9eb4ef85aae0"
    gg_api_res = requests.get(url)
    gg_api_data = gg_api_res.json()
    # print(data)
    comments = Comment.objects.filter(project_id=pid)  # .order_by('-rated', '-created')
    project_rating = project_calculated_rating(pid)

    context = {
        'gg_api_data': gg_api_data,
        'pid': pid,
        'comments': comments,
        'project_rating': project_rating
    }
    return render(request, 'charityfinder_app/project.html', context)


@login_required  # alt: request.user.is_authenticated check
def new_comment(request, pid):
    if request.method == 'POST':
        text = request.POST['newComment']
        comment = Comment()
        comment.body = text
        comment.author = request.user
        comment.project_id = pid
        if "reply" in request.POST:
            comment.parent = Comment.objects.get(pk=request.POST['reply'])
        comment.save()
        print('comment saved')
        return redirect(reverse('charityfinder_app:project', args={pid}))
    else:
        print('not authorized to comment')


@login_required
def new_comment_rating(request, pid):
    if request.method == 'POST':
        # "defaults" only execute when create, created = boolean
        # also protects against race conditions
        rated, created = UserCommentRating.objects.get_or_create(
            user=request.user,
            comment=Comment.objects.get(pk=request.POST['reply']),
            defaults={'state': request.POST['comment_rating']},
        )
        if not created:
            rated.state = request.POST['comment_rating']
            rated.save()
            print('comment rating updated')
        else:
            print('comment rating created')
        return redirect(reverse('charityfinder_app:project', args={pid}))
    else:
        print('not authorized to vote')


@login_required
def delete_comment(request, pid):
    if request.method == 'POST':
        comment = get_object_or_404(Comment, author=request.user, pk=request.POST['reply'])
        comment.body = 'Deleted'
        comment.save()
        print('comment deleted')
        return redirect(reverse('charityfinder_app:project', args={pid}))
    else:
        print('not authorized to delete')


@login_required
def new_project_vote(request, pid):
    if request.method == 'POST':
        rated, created = UserProjectRating.objects.get_or_create(
            user=request.user,
            project_id=pid,
            defaults={'rating': request.POST['project_rating']},
        )
        if not created:
            rated.rating = request.POST['project_rating']
            rated.save()
            print('project rating updated')
        else:
            print('project rating created')
        return redirect(reverse('charityfinder_app:project', args={pid}))
    else:
        print('not authorized to vote')
