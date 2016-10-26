from django.db import models

# Create your models here.

class Groups(models.Model):
    group_name = models.CharField(max_length=100)

    def __str__(self):
        return self.group_name

class Hosts(models.Model):
    host_name = models.CharField(max_length=100)
    host_ip = models.CharField(max_length=100)
    Groups = models.ForeignKey(Groups, on_delete=models.CASCADE)

    def __str__(self):
        return self.host_name





