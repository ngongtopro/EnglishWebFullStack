from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class Question(models.Model):

    quest_text = models.CharField(max_length=200)
    pub_data = models.DateTimeField('date_published')

    def __str__(self):
        return self.quest_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_data <= now

    was_published_recently.admin_order_field = 'pub_data'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
