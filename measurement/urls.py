from django.contrib import admin
from django.urls import path
# from measurement.views import sensor
# from measurement.views import measurement
from measurement.views import SensorView
from measurement.views import SensorView1
from measurement.views import MeasurementView

from measurement.views import SensorUpdateAPIView
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SensorUpdateAPIView.as_view()),
    path('measurements/', MeasurementView.as_view()),
    # path('sensors/<pk>/', SensorView1.as_view()),
    # path('measurements/<pk>/', SensorUpdateAPIView.as_view()),

    
    
    # path('', measurement),
    # TODO: зарегистрируйте необходимые маршруты
]
