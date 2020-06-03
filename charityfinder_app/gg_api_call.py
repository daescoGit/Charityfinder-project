from django.core.cache import cache
from django.conf import settings
import requests


# refine (try-except)
# using low-level cache to only cache the external api call
# not comments, too dynamic
def gg_call_project(pid, query):
    if cache.get(f"project_{pid}"):
        print('gg api loaded from cache')
    else:
        url = f"{query}{pid}.json?api_key={settings.GG_API_KEY}"
        gg_api_res = requests.get(url)
        gg_api_data = gg_api_res.json()
        # using add here instead of .set (only add if doesn't exist)
        # to not refresh the cache countdown (forcing api call every (x)sec to check for updates)
        cache.add(f"project_{pid}", gg_api_data, 1800)
        print('gg api cache expired')
    return cache.get(f"project_{pid}")


def gg_call_project_list(query):
    if cache.get('projects'):
        print('gg api loaded from cache')
    else:
        url = f"{query}.json?api_key={settings.GG_API_KEY}"
        gg_api_res = requests.get(url)
        gg_api_data = gg_api_res.json()
        cache.add('projects', gg_api_data, 30)
        print('gg api cache expired')
    return cache.get('projects')
