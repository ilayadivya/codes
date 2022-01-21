from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import db

class HelloView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request):
		name=request.GET.get("name", None)
		if name==None:
			content = {'result': 'false','message':"name is missing"}
		else:
			#content=name

			content = {'result': 'true','data':db.getbankByIfsc(name)}
		return Response(content)

class Branch(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request):
		city=request.GET.get("city", None)
		name=request.GET.get("bank", None)
		if name==None or city==None:
			content = {'result': 'false','message':"pharm is missing","city":city,"bank":name}
		else:
			#content=name

			content = {'result': 'true','data':db.getbankBycity(city,name)}
		return Response(content)
# Create your views here.
