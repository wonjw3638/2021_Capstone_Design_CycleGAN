from django.contrib import admin

# Register your models here.
# superuser 
# Username : jiwon
# Password : asdf1215

from .models import ImageUpload  
admin.site.register(ImageUpload)  

from .models import Image
admin.site.register(Image)


