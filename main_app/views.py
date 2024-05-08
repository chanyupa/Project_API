from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
class ProjectApiView(APIView):
    serializer_project=ProjectSerializer
    def get(self,request):
        info  = Project.objects.all().values()
        return Response({"Your Account Info": info})

    def post(self,request):
        serializer_post_project=ProjectSerializer(data=request.data)
        if(serializer_post_project.is_valid()):
            Project.objects.create(id=serializer_post_project.data.get("id"),
                            name=serializer_post_project.data.get("name"),
                            password=serializer_post_project.data.get("password"),
                            age=serializer_post_project.data.get("age"),
                            address=serializer_post_project.data.get("address"),
                            gender=serializer_post_project.data.get("gender"),
                            )

        project = Project.objects.all().filter(id=request.data["id"]).values()
        return Response({"Notification": "New Account is Added!", "Project": project})
