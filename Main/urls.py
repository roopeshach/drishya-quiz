from django.urls import path
from . import views

urlpatterns = [
    path('round/<int:round_id>/question/<int:question_id>/user/<int:user_id>', views.GameView.as_view(), name="Game"),
    path('check-answer', views.answer_checker, name="CheckAnswer"),
    path('', views.index, name="Index"),
    path('leaderboard', views.user_score, name="Leaderboard"),
    path('start-game/<int:round_id>', views.start_game, name="StartGame"),
    path('check_serial', views.check_serial, name="CheckSerial"),
    path('options/<int:id>', views.options, name="options")

    
    
]
