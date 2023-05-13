from django.db import models
from datetime import datetime

class Author(models.Model):
    user = models.CharField(max_length=200)
    post = models.CharField()
    quantity_post = models.IntegerField(default=0)
    raing = models.IntegerField(default=0)




economy = 'EC'
politician = 'PL'
worldnews = 'WN'
hostnews = 'HN'
sport = ' SP'

POSITION = [
    (economy, 'Экономика'),
    (politician, 'Политика'),
    (worldnews, 'Мировые новости'),
    (hostnews, 'Местные новости'),
    (sport, 'Спортивные новости')
]


class Category(models.Model):
    category = models.CharField(max_length=2, choices=POSITION, default='HN')

class Post(models.Model):
    name_news = models.BigAutoField(max_length=100)
    date_in = models.DateField(auto_now_add=True)
    date_out = models.DateField(auto_now_add=True)
    category = models.CharField(default=True)
    header = models.CharField(max_length=255)
    contents = models.TextField()
    comment = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    post = models.ManyToManyField('Post', through='Postcotegory')

    def get_last_name(self):
        return self.post.user

    def get_duration(self):
        if self.complete:
            return (self.date_out - self.date_in).total_second() // 60
        else:
            return (datetime.now(timezone.utc) - self.date_in).total_seconds() // 60

class Postcotegory(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

    def post_sum(self):
        post_quantity = self.post.quantity_post
        return post_quantity * self.amount

class Comment(models.Model):
    pass
