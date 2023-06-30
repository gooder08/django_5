from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Measurement(models.Model):
    # sensor = models.CharField(max_length=50)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.FloatField()
    date = models.DateTimeField (auto_now=True)
    # time = models.TimeField(auto_now=True)
    

