from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from enum import Enum


# ENUM class
class ErcProtocols(Enum):
    ECR20 = 1
    ECR721 = 2
    ECR1155 = 3


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
    context['result'] = ["ECR20", "ECR721", "ECR1155"]
    context['status'] = status.HTTP_200_OK
    return Response(context, status=status.HTTP_200_OK)
