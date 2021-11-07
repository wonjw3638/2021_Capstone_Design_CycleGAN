from django import forms
from .models import ImageUpload

class UploadForm(forms.ModelForm):
    
    class Meta:
        model = ImageUpload
        fields = {'title', 'pic'}

##crop

from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('file',)