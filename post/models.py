from django.db import models
from account.models import User
# Create your models here.


def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)


class Post(models.Model):
    content = models.TextField()    
    image = models.ImageField(upload_to='posts/' , null =True , blank=True)
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.content[:100]


    @property
    def get_comments(self):
        return Comment.objects.filter(post__id=self.id)
        
    @property
    def total_likes(self):
        return Like.objects.filter(post__id=self.id).count()

    @property
    def total_comments(self):
        return Comment.objects.filter(post__id=self.id).count()


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE )
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    post = models.ForeignKey(Post, on_delete=models.CASCADE )
    created_at = models.DateTimeField(auto_now_add=True)