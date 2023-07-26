from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status


@api_view(['POST',])
def registertion_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            refresh = RefreshToken.for_user(account)
            data['response'] = 'registeration successful'
            data['username'] = account.username
            data['email'] = account.email
            data['token1'] = {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                        }
        else:
            data = serializer.errors
        return Response(data , status = status.HTTP_201_CREATED)
