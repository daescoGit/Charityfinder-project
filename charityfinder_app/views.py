from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.cache import cache
from .gg_api_call import gg_call_project

from .models import UserProjectRating, project_calculated_rating
from comment_app .models import Comment


def index(request):
    return render(request, 'charityfinder_app/index.html')


def project_detail(request, pid):
    query = 'https://api.globalgiving.org/api/public/projectservice/projects/'
    gg_call_project(pid, query)

    comments = Comment.objects.filter(project_id=pid)
    project_rating = project_calculated_rating(pid)

    context = {
        'gg_api_data': cache.get(f"project_{pid}"),
        'pid': pid,
        'comments': comments,
        'project_rating': project_rating
    }
    return render(request, 'charityfinder_app/project.html', context)


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
