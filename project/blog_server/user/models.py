from django.db import models

# Create your models here.

class UserProfile(models.Model):
        username = models.CharField(max_length=11, verbose_name=u'用户名', primary_key=True)
        nickname = models.CharField(max_length=30, verbose_name=u'昵称')
        email = models.CharField(max_length=50, verbose_name=u'邮箱')
        password= models.CharField(max_length=40, verbose_name=u'密码')
        sing = models.CharField(max_length=50, verbose_name='个人签名')
        info = models.CharField(max_length=50, verbose_name='个人描述')
        avatar = models.ImageField(upload_to='avatar/')

        class Meat:

            db_table = 'user_profile'
