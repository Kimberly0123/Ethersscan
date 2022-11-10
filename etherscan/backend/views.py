from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from enum import Enum


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


@csrf_exempt
@api_view(["GET"])
def accounts(request):
    """
    /accounts
    """
    context = {}
    return Response(context, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def contracts(request, id):
    """
    /contracts/{id}
    """
    context = {}
    return Response(context, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def contracts(request):
    """
    /contracts?token_name={token_name}&erc={erc}?acount={account}
    """
    context = {''}

    print(request.query_params.get('name'))

    return Response(context, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def contracts(request):
    """
    /tokens/{id}/?contract={contractId}
    """
    context = {''}

    print(request.query_params.get('name'))

    return Response(context, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def contracts(request):
    """
    /tokens/{id}/?contract={contractId}
    """
    context = {''}

    print(request.query_params.get('name'))

    return Response(context, status=status.HTTP_200_OK)
