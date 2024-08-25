from django.http import HttpResponse
from django.contrib.auth.models import User


class SubdomainMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().split(".")
        if len(host) > 2:
            subdomain = host[0]
            try:
                user = User.objects.get(username=subdomain)
                request.user = user
            except User.DoesNotExist:
                return HttpResponse("User not found", status=404)
        return self.get_response(request)
