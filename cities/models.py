from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Region(models.Model):
    region_name=models.CharField(max_length=255)
    def __str__(self):
        return self.region_name



class Classification(models.Model):
    classification_name=models.CharField(max_length=255)
    def __str__(self):
        return self.classification_name
        
# class City(models.Model):
#     name = models.CharField(max_length=255)
#     state = models.CharField(max_length=255)

#     class Meta:
#       verbose_name_plural = "cities"

#     def __str__(self):
#         return self.name
        

class Intity(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    region = models.ForeignKey(Region,on_delete=models.CASCADE)
    intities_pic=models.FileField(upload_to='images')
    created=models.DateField()
    classification=models.ForeignKey(Classification,on_delete=models.CASCADE)
    works=models.TextField(default="")
    abstract=models.TextField(default="")
    permission=models.FileField(upload_to='images')

    class Meta:
      verbose_name_plural = "intities"
    def __str__(self):
        return self.name