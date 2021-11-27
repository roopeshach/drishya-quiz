from django.urls import path
from . import views

urlpatterns = [
    path('round/<int:round_id>/question/<int:question_id>', views.GameView.as_view(), name="Game"),
    path('check-answer', views.answer_checker, name="CheckAnswer"),
    path('', views.index, name="Index"),
    
    
]
