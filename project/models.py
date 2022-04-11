from django.db import models
# from post.models import Post
# from django.contrib.auth.models import User

# Create your models here.


class projects(models.Model):

    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1500)
    image_url = models.CharField(max_length=520)

    def __str__(self):
        return self.name

#    class Comment(models.Model):
        #  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
        #  user = models.ForeignKey(User, on_delete=models.CASCADE)
        #  body = models.TextField()
        #  date = models.DateTimeField(auto_now_add=True)
