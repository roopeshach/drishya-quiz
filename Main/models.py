from django.db import models

# Create your models here.

#quiz application models

#category model
class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name



class Round(models.Model):
    name = models.CharField(max_length=100)
    time = models.IntegerField(default=1)
    def __str__(self):
        return self.name

    def first_question(self):
        question = Question.objects.filter(round=self).first()
        return question
        

#question model
class Question(models.Model):
    question_text = models.TextField()
    pub_date = models.DateTimeField('date published')
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='questions', height_field=None, width_field=None, max_length=None, blank=True)
    music = models.FileField(upload_to='music_files/', blank=True)
    score = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.question_text

#answer model
class Answer(models.Model):
    index_choices = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    )
    index = models.CharField(max_length=3, choices=index_choices)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    def __str__(self):
        return self.answer_text

#user model
class User(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name



