from django.db import models

# Create your models here.
class Brands(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




class Cars(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150,default='bmw@gmail.com')
    photo = models.ImageField(upload_to="post/photos/",null=True,blank=True)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)

    def __str__(self):
        return self.name