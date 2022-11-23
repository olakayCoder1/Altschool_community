from django.db import models
from django.conf import settings
from django.urls import reverse
from account.models import User
# Create your models here.





class Threads(models.Model):
    CHAT_TYPE = [ 
        ('direct','direct'),
        ('group', 'group')
    ]
    name = models.CharField(max_length=100, unique=True)
    thread_type = models.CharField(max_length=200, choices=CHAT_TYPE )
    created_at = models.DateTimeField(auto_now_add=True)
    discription = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('group_chat', args=[self.name.split('_')[1]])

    



class Messages(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL , null=True)
    thread_name = models.ForeignKey(Threads, on_delete=models.CASCADE)
    content = models.TextField(null=True)
    image = models.ImageField(upload_to='chats/', null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


