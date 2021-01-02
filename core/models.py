from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

import mistune

# Create your models here.
User = get_user_model()


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now=True)
    question = models.TextField()
    question_html = models.TextField(editable=False, default='', blank=True)
    attachment = models.FileField(blank=True)
    tag = models.CharField(max_length=256, null=True, blank=True, default='None')

    def save(self, *args, **kwargs):
        self.question_html = mistune.html(self.question)
        super().save(*args, *kwargs)

    def __str__(self):
        return str(self.title)

    @staticmethod
    def get_absolute_url():
        return reverse_lazy('core:all-questions')

    class Meta:
        ordering = ['-date']


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    answer = models.TextField()
    answer_html = models.TextField(editable=False, default='', blank=True)

    def __str__(self):
        return str(self.answer)

    @staticmethod
    def get_absolute_url():
        return reverse_lazy('core:all-questions')
