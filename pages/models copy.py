from django.db import models

# Create your models here.

class ImageUpload(models.Model):
    
    title = models.CharField(max_length=20)

    pic = models.ImageField(null=True, blank=True, upload_to="")

    def __str__(self):
        return self.title

### 210906 

## 211021
class Image(models.Model):
    file = models.ImageField(upload_to="")
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)
        


