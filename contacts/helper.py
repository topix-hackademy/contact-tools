from rest_framework import status
from rest_framework.response import Response
from .models import Service
import logging


logger = logging.getLogger('ct-logger')


def auth_decorator(f):
    def inner(request, *args, **kwargs):
        try:

            auth_token = request.META['HTTP_AUTH_TOKEN']
            authorized_app = Service.objects.get(token=auth_token)
            message = "[%s %s] called by %s" % (request.META['REQUEST_METHOD'], request.META['PATH_INFO'],
                                                 authorized_app.service_name )
            logger.info(message)
        except Exception as e:
            content = {"message": "Permission denied"}
            message = "[%s %s] error %s from %s" % (request.META['REQUEST_METHOD'], request.META['PATH_INFO'],
                                                    content.get('message'), request.META['REMOTE_ADDR'])
            logger.error(message)
            return Response(content, status=status.HTTP_403_FORBIDDEN)
        return f(request, *args, **kwargs)

    return inner
