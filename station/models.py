from django.db import models

class Station(models.Model):  
    Date = models.DateField(max_length=100)  
    Time = models.CharField(max_length=100)  
    RTCTemp = models.FloatField(max_length=100)  
    Temp = models.FloatField(max_length=100)
    Humidity = models.FloatField(max_length=100) 
    Pressure = models.FloatField(max_length=100)
    PM2_5 = models.FloatField(max_length=100)
    PM10 = models.FloatField(max_length=100)
    
    class Meta:  
        db_table = "station"  
        
