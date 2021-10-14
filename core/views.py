from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

class IndexView(APIView):
	permission_classes = (AllowAny,)
	def get(self, requset):
		content = {'Get Access/Refresh token': "http://127.0.0.1:8000/api/token/",
					'Refresh Token' : 'http://127.0.0.1:8000/api/token/refresh/',
					'Token Verify' : 'http://127.0.0.1:8000/api/token/verify/'
				}
		return Response(content)

