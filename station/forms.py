from django import forms  
from station.models import Station  
class StationForm(forms.ModelForm):  
    class Meta:  
        model = Station  
        fields = "__all__" 