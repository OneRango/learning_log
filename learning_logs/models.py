from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """用户学习的主题   """
    text = models.CharField(max_length=200) #存储一个字符或者文本的数据 最大限制为200字符
    date_added = models.DateTimeField(auto_now_add=True)    #存储时间日期的数据创建新的主题 自动记录当前时间
    owner = models.ForeignKey(User,on_delete=models.DO_NOTHING)#用户外键
    
    def __str__ (self):
        """返回模型的字符串表示"""
        return self.text

class Entry(models.Model):
    """学到的某个主题的具体知识"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)#必须传递on_delete
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__ (self):
        return self.text[:50] + "..."