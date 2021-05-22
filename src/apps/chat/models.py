from django.db import models

class ChatModel(models.Model):
    room_no = models.CharField(max_length=10)
    message = models.TextField()
