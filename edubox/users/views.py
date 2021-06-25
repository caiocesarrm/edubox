from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from rest_framework import generics
from rest_framework.permissions import AllowAny
from edubox.users.serializers import CreateAuthUserSerializer
from django.contrib.auth.models import Group
from rest_framework.response import Response
from edubox.users.services import services
from rest_framework import status

User = get_user_model()

class CreateAuthUserView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    model = User
    serializer_class = CreateAuthUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = CreateAuthUserSerializer(data=request.data.copy())
        serializer.is_valid(raise_exception=True)
        try:
            result = services.UserRegister.execute(**serializer.validated_data)
        except Exception as e:
            return Response({'success':False, 'message':'Something gone wrong.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        if result['success']:
            return Response(result, status=status.HTTP_201_CREATED)
        else:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)



