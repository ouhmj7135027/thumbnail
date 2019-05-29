from django.db import models
from imagekit.models import ImageSpecField # 썸네일 만들 수 있게 해줌 
from imagekit.processors import ResizeToFill # 썸네일 크기 조정
 
class Picture(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="img")
    objects = models.Manager()
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(80, 80)])

    def __str__(self):
        return self.text


