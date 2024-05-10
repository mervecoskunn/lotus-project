from django.db import models
from django.utils import timezone
import os

# Create your models here.


class Post(models.Model):
    img = models.ImageField(upload_to='posts', null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def delete(self, *args, **kwargs):
        # Delete the image file associated with the post
        if self.img:
            if os.path.isfile(self.img.path):
                os.remove(self.img.path)
        # Call the parent class' delete method to delete the Post instance
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title
