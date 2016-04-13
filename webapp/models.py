from django.db import models

class Image(models.Model):
    # Image_Number = models.IntegerField()
    Likes = models.IntegerField(null=True)
    User = models.TextField(null=True)
    image_url = models.TextField(null=True)
    image_link = models.TextField(null=True)
    image_datatype = models.TextField(null=True)
    post_date = models.DateField(null=True)
    # tag = models.TextField(null=True)

    def __str__(self):
        return self.User