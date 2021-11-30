from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Round)
admin.site.register(User)

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    model = Question



admin.site.register(Question, QuestionAdmin)

admin.site.register(Answer)
admin.site.register(Category)