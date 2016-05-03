from django.db import models

class Location(models.Model):
    description = models.CharField(max_length = 32)
    created_on = models.DateTimeField()

    def __str__(self):
        return self.description

class Role(models.Model):
    description = models.CharField(max_length = 32)
    created_on = models.DateTimeField()

    def __str__(self):
        return self.description

class Card(models.Model):
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    role = models.ForeignKey(Role, on_delete = models.CASCADE)
    likes = models.IntegerField(default = 0)
    dislikes = models.IntegerField(default = 0)

    def __str__(self):
        return str(self.location) + " | " + str(self.role)
