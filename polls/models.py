from django.db import models

# Create your models here.

from django.db import models


class PastQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def get_choices(self):
        return self.pastchoice_set.all()


class PastChoice(models.Model):
    question = models.ForeignKey(PastQuestion, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def increment_vote(self):
        self.votes += 1
        self.save()


class PresentQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def get_choices(self):
        return self.presentchoice_set.all()


class PresentChoice(models.Model):
    question = models.ForeignKey(PresentQuestion, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def increment_vote(self):
        self.votes += 1
        self.save()


class FutureQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def get_choices(self):
        return self.futurechoice_set.all()


class FutureChoice(models.Model):
    question = models.ForeignKey(FutureQuestion, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def increment_vote(self):
        self.votes += 1
        self.save()
