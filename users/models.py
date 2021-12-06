from django.db import models


#class User:

   # def __init__(self, username, e_mail):

    #    self.username = username
    #    self.e_mail = e_mail

class User(models.Model):
    username = models.CharField(max_length=200)
    e_mail = models.EmailField(max_length=100)