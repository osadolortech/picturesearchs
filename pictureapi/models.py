from django.db import models

# Create your models here.
def upload_to(instance, filename):
    return 'image/{filename}'.format(filename=filename)


class PictureModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_to, default='image/default.jpg')
    uploaded_date = models.DateTimeField(auto_now_add=True)