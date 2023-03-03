from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    email=models.EmailField(unique=True)
    is_employee=models.BooleanField(default=False)
    is_user=models.BooleanField(default=True)


from django.db import models
# Create your models here.


class StudentForm(models.Model):
    STATUS=(
        ('submitted','submitted'),
        ('pending','pending'),
        ('resolved','resolved')
    )

    
    user=models.ForeignKey(MyUser,null=True,on_delete=models.CASCADE)
    fullname=models.CharField(max_length=100,null=True)
    area=models.CharField(max_length=10,null=True)
    status=models.CharField(max_length=100,null=True,choices=STATUS)
    image=models.ImageField(null=True,blank=True)

    def __str__(self):
        return f"{self.fullname}"