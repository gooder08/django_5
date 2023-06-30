# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Sensor
from .models import Measurement
from .serializers import SensorSerializer
from .serializers import MeasurementSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import RetrieveUpdateAPIView

# @api_view(['GET', 'POST'])
# def sensor(request):
#     if request.method == 'GET':
#         sensor = Sensor.objects.all()
#         data = SensorSerializer(sensor, many=True)
#         return Response(data.data)
#     if request.method == 'POST':
#         return Response({'ggg':'jo'})

# @api_view(['GET'])
# def measurement(request):
#     measurement = Measurement.objects.all()
#     data = MeasurementSerializer(measurement, many=True)
#     return Response(data.data)

class SensorView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    # def patch(self, request):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
    
    
class SensorView1(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class MeasurementView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    def post(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
# class MeasurementView(RetrieveAPIView):
#     queryset = Measurement.objects.all()
#     serializer_class = MeasurementSerializer