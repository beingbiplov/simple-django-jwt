from rest_framework.views import APIView
from rest_framework.response import Response


class IndexView(APIView):
	def get(self, requset):
		content = {'msg': "Hello there!! Just checking."}
		return Response(content)