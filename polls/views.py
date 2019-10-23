from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import JsonResponse
from django.core import serializers
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


# AJAX version
def indexJSON(request):
    latest = Question.objects.filter(pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]
    latest_json = serializers.serialize("json", latest)
    return JsonResponse(latest_json, safe=False)
            

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
    

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    

def vote(request, question_id):
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
        return HttpResponseRedirect(reverse('polls:results',
                                            args=(question.id,)))

# AJAX version
def voteJSON(request, question_id):
    result = "failure"
    if request.method=="POST" and "choice" in request.POST:
        try:
            question = Question.objects.get(pk=question_id);
            selected_choice = question.choice_set.get(
                pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            pass
        else:
            selected_choice.votes += 1
            selected_choice.save()
            result = "success"
    return JsonResponse({"success": result}, safe=False)
                                                                
