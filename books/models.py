from django.db import models

# Create your models here.


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32,verbose_name='书名')
    author = models.CharField(max_length=32,verbose_name='作者')
    is_break = models.BooleanField(default=False,verbose_name='是否借出')
    user_id = models.IntegerField(default=0,verbose_name='借出人')
    break_date = models.DateTimeField(null=True,blank=True,verbose_name='借出时间')
    return_date = models.DateTimeField(null=True,blank=True,verbose_name='还书时间')

    class Meta:
        db_table = 'book'
        verbose_name = '图书'

