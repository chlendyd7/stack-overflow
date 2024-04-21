from rest_framework import generics,viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from common.exceptions import RaiseError
from service.services.user import UserService
from service.models.user import User
from service.serializers.user import UserSerializer
from rest_framework.decorators import action
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    authentication_classes = []
    permission_classes = []
    queryset=User.objects.none()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # JWT 토큰 생성
        refresh = RefreshToken.for_user(user)
        tokens = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        return Response(tokens)

class UserViewSet(viewsets.ModelViewSet):
    authentication_classes=[JWTAuthentication]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination

    @action(
        methods=['POST'],
        detail=False,
        url_path='sign-in',
        authentication_classes=[],
        permission_classes=[],
    )
    def signin(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        try: 
            token = UserService.singin(username, password)
        except RaiseError as e:
            return Response(
                status=e.code,
                data={'message':e.message},
            )

        return Response(
            dict(
                access = str(token.access_token),
                refresh = str(token),
            )
        )
