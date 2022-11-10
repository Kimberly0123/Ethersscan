from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@csrf_exempt
@api_view(["GET"])
def ercprotocols(request):
    """ Get all NFT protocol (ENUM) 

    :method GET
    :param request:
    :return:
        :: status = 200 (OK)
        :: result: [{value: ,name: }]
    """
    context = {}
    if request.method == "GET":

        return Response(context, status=status.HTTP_200_OK)
