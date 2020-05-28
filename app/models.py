from django.db import models

# Create your models here.


class UserProfile(models.Model):
     id = models.AutoField(primary_key=True, verbose_name='主键自增')
     username = models.CharField(max_length=12, verbose_name='用户名')
     password = models.CharField(max_length=36, verbose_name='密码')
     # is_active = models.BooleanField(default=False, verbose_name='激活状态')

     def __str__(self):
        return "<{}>".format(self.username)

     class Meta:
        db_table = "UserProfile"



