from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import timeit

from .models import Question, Choice, Entry


"""
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
"""


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """return the last five published"""
        return Question.objects.filter(
                pub_date__lte=timezone.now()
            ).order_by('-pub_date')[:5]


"""
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
"""


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


"""
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
"""


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # display again the question voting form
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't selected a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # return httpresponseredirect after success save
        # prevent data from being posted twice if a user hit back button
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


class TimeitTestView(generic.DetailView):
    template_name = 'polls/timeittest.html'
    context_object_name = 'object_list'

    def get_object(self, queryset=None):
        start_time = timeit.default_timer()
        query_test = Entry.objects.all()

        [entry for entry in query_test]

        print(query_test[0])
        print(query_test[1])
        print(query_test[3])
        print(query_test[3])
        print(query_test[3])
        print(query_test[3])
        print(query_test[3])
        print(query_test[3])
        print(query_test[3])
        print(query_test[6])

        elapsed = timeit.default_timer() - start_time
        return "elapsed time: %f" % (elapsed * 1000)




