from rest_framework import status
from rest_framework.response import Response
from .models import Service


def auth_decorator(f):
    def inner(request, *args, **kwargs):
        try:
            auth_token = request.META['HTTP_AUTH_TOKEN']
            authorized_app = Service.objects.get(token=auth_token)
        except Exception as e:
            content = {"message": "Permission denied"}
            return Response(content, status=status.HTTP_403_FORBIDDEN)
        return f(request, *args, **kwargs)

    return inner
