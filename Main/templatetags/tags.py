from Main.models import Question, Round

from django import template

register = template.Library()

#get first question of round
@register.simple_tag
def first_question(round_id):
    round_id = int(round_id)
    if Question.objects.filter(round=round_id).exists():
        question = Question.objects.filter(round=round_id).first()
        return question.id
    else:
        return None

@register.simple_tag
def ordinal(number):
    ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
    return ordinal(number)


register.filter('first_question', first_question)
register.filter('ordinal', ordinal)