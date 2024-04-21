from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from common.exceptions import RaiseError

class UserService:
    
    def singin(username, password):
        user = authenticate(username=username, password=password)
        if not user:
            raise RaiseError('입력이 잘못되었습니다', 400)
        
        refresh = RefreshToken.for_user(user)
        
        return refresh
