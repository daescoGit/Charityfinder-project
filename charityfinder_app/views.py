from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import requests
from django.urls import reverse

from .models import UserProjectRating, project_calculated_rating
from comment_app .models import Comment


def index(request):
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
