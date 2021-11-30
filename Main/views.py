from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
from .models import *
from .forms import *

from django.views.generic.edit import UpdateView , CreateView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin


#Game View
class GameView(CreateView,LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        login_url = 'login/'
        return(self.request.user)

    
    def get(self,request, round_id, question_id):
        round_id = int(round_id)
        question_id = int(question_id)
        round = Round.objects.get(id=round_id)
        question = Question.objects.get(id=question_id)
        answers = Answer.objects.filter(question=question)
        next_question = Question.objects.filter(round=round).filter(id__gt=question_id).filter(is_active=True).first()
        previous_question = Question.objects.filter(round=round).filter(id__lt=question_id).filter(is_active=True).last()
        users = User.objects.all()
        context = {
            'round': round,
            'question' : question,
            'answers' : answers,
            'next_question' : next_question,
            'previous_question' : previous_question,
            'users' : users,

        }

        return render(request, 'Main/index.html', context)
    def post(self, request, round_id, question_id):
        answer_id = request.POST.get('answer_id')
        answer = Answer.objects.get(id=answer_id)
        user_id = request.POST.get('user_id')
        user = User.objects.get(id=user_id)
        round_id = int(round_id)
        question_id = int(question_id)
        round = Round.objects.get(id=round_id)
        question = Question.objects.get(id=question_id)
        question.is_active = False
        answers = Answer.objects.filter(question=question)
        next_question = Question.objects.filter(round=round).filter(id__gt=question_id).filter(is_active=True).first()
        previous_question = Question.objects.filter(round=round).filter(id__lt=question_id).filter(is_active=True).last()
        users = User.objects.all()
        context = {
            'round': round,
            'question' : question,
            'answers' : answers,
            'next_question' : next_question,
            'previous_question' : previous_question,
            'users' : users,

        }

        if answer.correct:
            user.score += question.score
            context['response'] = True
            context['message'] = f'Congratulations {user.name} for scoring {question.score}.'
            return render(request, 'Main/index.html', context)
        else:
            context['response'] = False
            context['message'] = f'Sorry {user.name} you are wrong!'
            return render(request, 'Main/index.html', context)
        



#ajax answer checker
def answer_checker(request):
    if request.method == 'POST':
        answer_id = request.POST.get('answer_id')
        answer = Answer.objects.get(id=answer_id)
        question = answer.question
        question.is_active = False
        user_id = request.POST.get('user_id')
        user = User.objects.get(id=user_id)
        if answer.correct:
            user.score += question.score

            user.save()
            response = {
                'correct' : "True",
                'message' : f'Congratulations {user.name} for scoring {question.score}.'

            }
            return JsonResponse(response)
        else:
            response = {
                'correct' : "False",
                'message' : f' Try Harder! {user.name}'
            }
            return JsonResponse(response)
            
    else:
        return render(request, 'Main/answer_checker.html', {})
    
def index(request):
    rounds = Round.objects.all()
    #users order by score
    users = User.objects.order_by('-score')
    context = {
        'rounds' : rounds, 
        'users' : users,
    }
    return render(request, 'Main/main.html', context)
   