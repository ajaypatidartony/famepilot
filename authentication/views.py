from datetime import datetime

from rest_framework import status
from rest_framework.permissions import AllowAny
# from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from .renderers import UserJSONRenderer

from django.views.decorators.csrf import csrf_exempt
from .models import User

from .serializers import ( RegistrationSerializer , LoginSerializer , UserSerializer)

class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    renderer_classes = (UserJSONRenderer,)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

        
    def post(self, request):
        
        serializer = self.serializer_class(data=request.data)
        # print("test")
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


