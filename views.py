from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import CustomUser
from .serializers import RegisterSerializer, ConfirmationSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

@api_view(['POST'])
def confirm_user(request):
    serializer = ConfirmationSerializer(data=request.data)
    if serializer.is_valid():
        code = serializer.validated_data.get('code')
        try:
            user = CustomUser.objects.get(confirmation_code=code)
            user.is_active = True
            user.confirmation_code = ''
            user.save()
            return Response({'status': 'User confirmed'}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({'error': 'Invalid confirmation code'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

