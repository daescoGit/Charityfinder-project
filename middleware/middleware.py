from django.core.exceptions import PermissionDenied
import datetime


user_request_times = {}


# rudimentary post request limit
class AntiSpamMiddleware:
    # One-time configuration and initialization.
    # Executed when the WSGI server loads the app, not on each request
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before the view (and later middleware)
        if request.method == "POST":
            now = datetime.datetime.now()
            client_ip = request.META.get('REMOTE_ADDR')

            if client_ip not in user_request_times:
                user_request_times[client_ip] = {
                    'time': now,
                    'recent_reqs': 1,
                }
            else:
                dic = user_request_times[client_ip]
                # if prev time + 60s > now (under 60s passed)
                if dic['time'] + datetime.timedelta(seconds=60) > now:
                    dic['recent_reqs'] += 1
                    print(dic)
                    if dic['recent_reqs'] > 3:
                        raise PermissionDenied
                        # redirect to eg. captcha / gives timeout
                        print(dic)
                else:
                    dic['time'] = now
                    dic['recent_reqs'] = 1
                    print(user_request_times)

        # forwards the request to the next middleware or view function
        # get_response = next middleware / view
        response = self.get_response(request)

        # Code to be executed for each request/response after the view is called.

        return response
