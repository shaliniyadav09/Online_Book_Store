from django.db import models

class Enquiry(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100) 
    email = models.CharField(max_length=50) 
    contactno = models.CharField(max_length=15) 
    subject = models.CharField(max_length=300) 
    message = models.TextField()
    enqdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name}-{self.contactno}"
class LoginInfo(models.Model): #adminlogin
    usertype = models.CharField(max_length=14)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    status = models.CharField(max_length=20 , default='active')
    def __str__(self):
        return f"{self.username}-{self.usertype}"# show in djnago adminstration 


class UserInfo(models.Model):


    name = models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    contactno = models.CharField(max_length=15)
    address =models.TextField()
    profile=models.ImageField(upload_to='profiles/' ,null=True)
    login = models.OneToOneField(LoginInfo,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):#object ki id show krta h
        return f"{self.name}-{self.email}"