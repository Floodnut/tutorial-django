from django.shortcuts import render, get_object_or_404, redirect
#from django.http import HttpResponse
from django.utils import timezone
from .models import Question
from .forms import QuestionForm


# Create your views here.

def index(request):
    #return HttpResponse("test")
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pytest/question_list.html', context)

def detail(request,question_id):
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pytest/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    #answer = Answer(question=question, content=request.POST.get('content'),create_date=timezone.now())
    question.answer_set.create(content = request.POST.get('content'),create_date=timezone.now())
    return redirect('pytest:detail',question_id=question.id)

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question=form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pytest:index')
    else:
        form = QuestionForm()
    context = {'form':form}
    return render(request, 'pytest/question_form.html', context)