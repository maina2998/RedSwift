from django.db import models
from django.db.models.fields import CharField, PositiveSmallIntegerField

class Recipient(models.Model):
    first_name=models.CharField(max_length=20,default=None)
    last_name=models.CharField(max_length=20,default=None)
    age=models.PositiveSmallIntegerField(default=None)
    hospital=models.CharField(max_length=50,default=None)
    ward=models.CharField(max_length=30,null=True)
    location=models.CharField(max_length=100,default=None,blank=True,null=True)
    bloodgroup_choices=((u'AB negative',u'AB Negative',u'AB-'),
                        (u'B negative',u'B Negative',u'B-'),
                        (u'AB positive',u'AB Positive',u'AB+'),
                        (u'A negative',u'A Negative',u'A-'),
                        (u'O negative',u'O Negative',u'O-'),
                        (u'B positive',u'B Positive',u'B+'),
                        (u'A positive',u'A Positive',u'A+'),
                        (u'O positive',u'O Positive',u'O+'))
    blood_group=models.CharField(max_length=15,default=None,blank=True,null=True)
    blood_pints=models.CharField(max_length=10,default=None,blank=True,null=True)
    contact_person=models.CharField(max_length=100,default=None,blank=True,null=True)
    date=models.DateField(auto_now=True, null=True)




