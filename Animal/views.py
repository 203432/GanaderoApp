from django.shortcuts import render

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from asyncio import exceptions
import os.path

#Importaciones de modelos
from Animal.models import Animal

#Importaciones de serializadores
from Animal.serializers import AnimalSerializer

# Create your views here.
class AnimalList(APIView):
    def get(self,request,format=None):
        queryset=Animal.objects.all()
        serializer = AnimalSerializer(queryset,many=True,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer=AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            validated_data = serializer.validated_data
            img = Animal(**validated_data)
            # img.save()
            serializer_response = AnimalSerializer(img)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class AnimalDetail(APIView):
    def get_object(self, pk):
        try:
            return Animal.objects.get(pk=pk)
        except Animal.DoesNotExist:
            return 0
        
    def get(self, request, pk, format = None):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse  = AnimalSerializer(idResponse)
            return Response(idResponse.data, status=status.HTTP_200_OK)
        return Response("No se encontro el dato", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,pk, format=None):
        idResponse = self.get_object(pk)
        serializer = AnimalSerializer(idResponse, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        imagen = self.get_object(pk)
        if imagen != 0:
            imagen.delete()
            return Response("Dato eliminado",status=status.HTTP_204_NO_CONTENT)
        return Response("Dato no encontrado",status = status.HTTP_400_BAD_REQUEST) 