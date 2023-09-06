import datetime
from django.contrib import admin
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="date de creation", editable=False)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True, verbose_name="date de modification",
                                      editable=False)
    author = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="date de creation", editable=False)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True, verbose_name="date de modification",
                                      editable=False)

    def __str__(self):
        return self.choice_text
