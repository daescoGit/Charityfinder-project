from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import requests
from django.urls import reverse
from django.core.cache import cache
from django.conf import settings

from .models import UserProjectRating, project_calculated_rating
from comment_app .models import Comment


def index(request):
    return render(request, 'charityfinder_app/index.html')


# using low-level cache to only cache the external api call
# not comments, too dynamic
def project_detail(request, pid):
    # refine (try-except)
    if cache.get(f"project_{pid}"):
        print('gg api loaded from cache')
    elif not cache.get(f"project_{pid}"):
        url = f"https://api.globalgiving.org/api/public/projectservice/projects/{pid}.json?api_key={settings.GG_API_KEY}"
        gg_api_res = requests.get(url)
        gg_api_data = gg_api_res.json()
        # using add here instead of .set (only add if doesn't exist)
        # to not refresh the cache countdown (forcing api call every (x)sec to check for updates)
        cache.add(f"project_{pid}", gg_api_data, 30)
        print('gg api cache expired')
    else:
        print('broken')

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
