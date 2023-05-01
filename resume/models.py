from django.db import models

# Create your models here.

class Home(models.Model):
    file = models.FileField(upload_to='cv/', default="")
    title = models.CharField(max_length=100, default=True)
    issue = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    sn = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="")
    email = models.EmailField(max_length=254, default="")
    contact = models.IntegerField(default="")
    subject = models.CharField(max_length=25, default="")
    requirement = models.CharField(max_length=1000, default="")
    con_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  f' {self.sn}.  {self.name}'
    
    def save(self, *args, **kwargs):
        # do some custom processing here
        super(Contact, self).save(*args, **kwargs)