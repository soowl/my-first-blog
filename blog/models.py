from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model): # models.Models means Post is Django Model.   
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE) #models.ForeignKey – これは他のモデルへのリンク
    title = models.CharField(max_length=200) #models.CharField – 文字数が制限されたテキストを定義するフィールド
    text = models.TextField()#models.TextField – これは制限無しの長いテキスト用です。
    created_date = models.DateTimeField(default = timezone.now)#models.DateTimeField – 日付と時間のフィールド
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title    

    
