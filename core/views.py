from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class IndexView(APIView):
	permission_classes = (IsAuthenticated,)
	def get(self, requset):
		content = {'msg': "Hello there!! Just checking."}
		return Response(content)