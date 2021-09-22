from django.db import models
from utils.models import AbstractModel
from user_account.models import User
class Restaurant(AbstractModel):
        class Meta:
                db_table = 'restaurant'
        name=models.TextField(null=False,blank=False)
        address=models.TextField(null=False,blank=False)
        hot_line=models.CharField(max_length=16,null=True,blank=True)
        open_at=models.DateTimeField(auto_now_add=True,null=False)
        close_at=models.DateTimeField(auto_now_add=True,null=False)