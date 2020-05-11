from django.shortcuts import render
import requests


def project_detail_view(request, id):
    # refine
    url = f"https://api.globalgiving.org/api/public/projectservice/projects/{id}.json?api_key=79638b32-7812-44ef-b361-9eb4ef85aae0"
    api_res = requests.get(url)
    # api_res = requests.get('https://api.globalgiving.org/api/public/projectservice/all/projects/active.json?api_key=79638b32-7812-44ef-b361-9eb4ef85aae0') #&nextProjectId=1015
    data = api_res.json()
    # print(data)
    context = {
      'data': data
    }
    return render(request, 'charityfinder_app/project.html', context)
