from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from django.shortcuts import get_object_or_404

from automobile.models import Auto
from auto_api.serializers import AutoSerializer


class ListCreateAutoAPIView(APIView):
    """По url /autos получаем список автомобилей или методом post добавляем новую запись об автомобиле"""
    def get(self, request, *args, **kwargs):
        """Получение всех автомобилей из БД"""
        autos = Auto.objects.all()

        serializer = AutoSerializer(
            instance=autos,
            many=True,
        )

        return Response(data=serializer.data)

    def post(self, request: Request, *args, **kwargs):
        """Добавление записи об автомобиле в БД"""
        serializer = AutoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveUpdateDeleteAutoAPIView(APIView):
    """По url ***/autos/<int:pk>
    - получаем данные о конкретном автомобиле GET методом,
    - обновление данных о конкретном объекте через PUT/PATCH
    - удаление объекта БД по ПК"""
    def get(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        instance = get_object_or_404(Auto, **kwargs)

        serializer = AutoSerializer(instance=instance)

        return Response(data=serializer.data)

    def put(self, request: Request, * args, **kwargs):
        instance = get_object_or_404(Auto, **kwargs)

        serializer = AutoSerializer(instance=instance, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request: Request, * args, **kwargs):
        instance = get_object_or_404(Auto, **kwargs)

        serializer = AutoSerializer(instance=instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, * args, **kwargs):
        instance = get_object_or_404(Auto, **kwargs)

        instance.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
