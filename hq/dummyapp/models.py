from django.db import models

# Create your models here.
#create class for  test
class Test(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    user_image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name


    