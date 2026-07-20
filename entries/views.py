from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Entry
from .serializers import EntrySerializer, MyTokenObtainPairSerializer

class EntryViewSet(viewsets.ModelViewSet):
  queryset = Entry.objects.all()
  serializer_class = EntrySerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

  def perform_create(self, serializer):
    serializer.save(author=self.request.user)

class MyTokenObtainPairView(TokenObtainPairView):
  serializer_class = MyTokenObtainPairSerializer

  def post(self, request, *args, **kwargs):
    response = super().post(request, *args, **kwargs)
    refresh_token = response.data.pop('refresh')

    response.set_cookie(
      key='refreshToken',
      value=refresh_token,
      httponly=True,
      samesite='Lax',
      secure=False,
      path='/',
    )

    return response


class CookieTokenRefreshView(APIView):
  authentication_classes = []
  permission_classes = []

  def post(self, request):
    refresh_token = request.COOKIES.get('refreshToken')

    if not refresh_token:
      return Response(
        {'detail': 'Refresh Token이 없습니다.'},
        status=status.HTTP_401_UNAUTHORIZED,
      )

    try:
      refresh = RefreshToken(refresh_token)
      return Response({'access': str(refresh.access_token)})
    except TokenError:
      return Response(
        {'detail': 'Refresh Token이 만료되었거나 유효하지 않습니다.'},
        status=status.HTTP_401_UNAUTHORIZED,
      )


class LogoutView(APIView):
  authentication_classes = []
  permission_classes = []

  def post(self, request):
    response = Response({'detail': '로그아웃되었습니다.'})
    response.delete_cookie('refreshToken', path='/', samesite='Lax')
    return response
