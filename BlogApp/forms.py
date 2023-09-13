
from django import forms
from .models import *

class blogform (forms.ModelForm):
    class Meta:
        model = Blog    
        fields = '__all__'

class commentform(forms.ModelForm):
    class Meta:
        model = Comment_section
        fields = "__all__"

class shareform(forms.ModelForm):
    class Meta :
        model = Share_blg
        fields= "__all__"