from collections import OrderedDict

from django.http import Http404, HttpResponseRedirect

from rest_framework import exceptions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


@api_view(['GET'])
def index(request, format=None):
    """
    API Index
    /api/swagger/ -- Swagger
    """
    data = OrderedDict()
    return Response(data)
