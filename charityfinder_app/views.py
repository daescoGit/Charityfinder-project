from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests
from .models import Comment


# @login_required
def index(request):
    context = {

    }
    return render(request, 'charityfinder_app/index.html', context)


def project_detail_view(request, pid):
    # refine
    url = f"https://api.globalgiving.org/api/public/projectservice/projects/{pid}.json?api_key=79638b32-7812-44ef-b361-9eb4ef85aae0"
    gg_api_res = requests.get(url)
    gg_api_data = gg_api_res.json()
    # print(data)
    comments = Comment.objects.filter(project_id=pid)

    if request.method == 'POST' and request.user.is_authenticated:
        text = request.POST['newComment']
        comment = Comment()
        comment.body = text
        comment.author = request.user
        comment.project_id = pid
        comment.save()
        print("comment saved")
    else:
        print("not auth")

    context = {
        'gg_api_data': gg_api_data,
        'pid': pid,
        'comments': comments
    }
    return render(request, 'charityfinder_app/project.html', context)
