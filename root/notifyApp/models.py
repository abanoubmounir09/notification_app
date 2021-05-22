from django.db import models

from django.contrib.auth.models import User
# Create your models here.



class Notifications(models.Model):
    notifiaction_type=models.IntegerField()
    to_user=models.ForeignKey(User,related_name="notification_to",on_delete=models.CASCADE,null=True)
    from_user=models.ForeignKey(User,related_name="notification_from",on_delete=models.CASCADE,null=True)
    comment=models.TextField(blank=True,null=True)
    date=models.DateTimeField(auto_now_add=True,verbose_name=("Created in"))
    user_has_seen=models.BooleanField(default=False)

