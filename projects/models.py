from django.db import models

class Projects(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=300)
    uri = models.URLField(max_length=200, default='http://me.com')

    def __str__(self):
        return self.title