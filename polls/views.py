from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from.models import PastQuestion, PresentQuestion, FutureQuestion, PastChoice, PresentChoice, FutureChoice


def vote_past(request):
    questions = PastQuestion.objects.all()
    return render(request, 'polls/vote.html', {'question': questions, 'question_type': 'past'})


def vote_present(request):
    questions = PresentQuestion.objects.all()
    return render(request, 'polls/vote.html', {'question': questions, 'question_type': 'present'})


def vote_future(request):
    questions = FutureQuestion.objects.all()
    return render(request, 'polls/vote.html', {'question': questions, 'question_type': 'future'})


@csrf_exempt
def submit_votes(request, question_type):
    if request.method == 'POST':
        try:
            for question_id in request.POST:
                if question_id.isdigit():
                    choice_id = request.POST.get(question_id)
                    if question_type == 'past':
                        choice = get_object_or_404(PastChoice, id=choice_id)
                    elif question_type == 'present':
                        choice = get_object_or_404(PresentChoice, id=choice_id)
                    else:
                        choice = get_object_or_404(FutureChoice, id=choice_id)
                    choice.increment_vote()
            # return JsonResponse({'status':'success'})
            return render(request,"polls/result.html")
        except Exception as e:
            return JsonResponse({'status': 'error','message': str(e)})
    else:
        return JsonResponse({'status': 'error','message': 'Invalid request method'})

# def result(request):
#     return None

