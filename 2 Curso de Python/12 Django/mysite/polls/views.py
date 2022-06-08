# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template import loader
from .models import Question, Choice


def index(request):
    """
    Versión corta con return() en lugar de HttpResponde()

    Notese la ausencia de loader.get_template

    def index(request):
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        context = {'latest_question_list': latest_question_list}
        return render(request, 'polls/index.html', context)
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    print("### Pintando el argumento request de la función")
    print(request)
    print(type(request))
    print("### Finalizando el pintado de request")
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    """
    Espera un objeto request y un integer.

    Devuelve o un error si no se encuentra la pregunta correspondiente al integuer
    o la plantilla detail.html para URLs tipo /polls/question_id
    """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist buddy")
    return render(request, 'polls/detail.html', {'question': question})

def vote(request, question_id):
    """
    Formulario de votación para /polls/question_id/vote
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    """
    Espera un objeto requeste y un integer.

    Devuelve un listado de las respuestas con su correspondiente número de votos
    para urls del tipo /polls/question_id/results
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})