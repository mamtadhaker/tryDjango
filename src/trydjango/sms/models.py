from django.db import models

# Create your models here.
class Message(models.Model):
    user_id = models.CharField(max_length=50)
    message_id = models.CharField(max_length=50)
    datetime = models.DateTimeField(default=False, auto_now=False, auto_now_add=False)
    sender = models.CharField(max_length=50)
    message_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    # def __str__(self):
    #     return self.userid