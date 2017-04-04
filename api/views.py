from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
"""
Send the message!
"""
@api_view(['POST'])
def send(request, format=None):
    return
