from rest_framework import serializers

class ProjectSerializer(serializers.Serializer):
    id=serializers.IntegerField(label="Enter Your id")
    name=serializers.CharField(label="Enter Your Name")
    password=serializers.CharField(label="Enter Your Password")
    age=serializers.CharField(label="Enter Your Age")
    address=serializers.CharField(label="Enter Your Address")
    gender=serializers.CharField(label="Enter Your Gender")