from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#topic类
class Topic(models.Model):
    #"用户学习的主题"
    text = models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)#注意这里的on_delete方法是书上没有的

    def __str__(self):
        return self.text

#entry类
class Entry(models.Model):
    #学习到的有关某个主题的具体知识
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        #当需要使用Entry的字符串时的返回，如果太长返回前50个字符
        if len(self.text)>50:
            return self.text[:50]+'...'
        else:
            return self.text