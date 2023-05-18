from django.db import models

class User(models.Model):
    name=models.CharField(max_length = 255 ,null=True , blank=True)
    address=models.CharField(max_length = 255 ,null=True , blank=True)
    phonenumber=models.CharField(max_length = 255 ,null=True , blank=True)
    introducer=models.CharField(max_length = 255 ,null=True , blank=True)
    age=models.CharField(max_length = 255 ,null=True , blank=True)
    birthdate=models.DateField(max_length = 255 ,null=True , blank=True)
    height=models.CharField(max_length = 255 ,null=True , blank=True)
    weight=models.CharField(max_length = 255 ,null=True , blank=True)
    #gender=models.CharField(max_length = 255 ,null=True , blank=True)
    #illness=models.CharField(max_length = 255 ,null=True , blank=True)
    explain=models.CharField(max_length = 255 ,null=True , blank=True)
    drug=models.CharField(max_length = 255 ,null=True , blank=True)
    visitdate=models.DateField(max_length = 255 ,null=True , blank=True)
    testresult=models.CharField(max_length = 255 ,null=True , blank=True)
    prescription=models.CharField(max_length = 255 ,null=True , blank=True)
    primarydiagnose=models.CharField(max_length = 255 ,null=True , blank=True)
    needmorevisit=models.CharField(max_length = 255 ,null=True , blank=True)
    needmorevisitdate=models.DateTimeField(max_length = 255 ,null=True , blank=True)
    #uploadimage=models.FileField(upload_to='uploads/', height_field=None, width_field=None, max_length=100 , null=True , blank=True)
    def __str__(self):
        return self.name