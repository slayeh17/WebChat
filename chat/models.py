from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class User(AbstractUser):
    pass

class Text(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="chat_user")
    sender = models.ForeignKey("User", on_delete=models.PROTECT, related_name="chat_sender")
    recipients = models.ManyToManyField("User", related_name="chat_recipients")
    chat_text = models.CharField(max_length=1400)
    timestamp = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
            "id": self.id,
            "sender": self.sender,
            "chat_text": self.chat_text,
            "timestamp": self.timestamp,
        }
