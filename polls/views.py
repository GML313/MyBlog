# -*- coding: utf-8 -*-
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from django.template import loader
from django.urls import reverse
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Question,Choice,UserInfo
from .forms import ItemForm

class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.all()
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]

'''
    latest_question_list = Question.objects.all()
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context,request))
'''
class DetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(DetailView):
    model = Question
    template_name = 'polls/detail.html'
'''
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'polls/detail.html',{'question':question})
'''
'''
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
'''
def vote(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error-message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
def showdb(request):
    if request.method == 'POST':
        new_name = request.POST['new_name']
        new_email = request.POST['new_email']
        new_telnum = request.POST['new_telnum']
        new_chinaid = request.POST['new_chinaid']
        UserInfo.objects.create(name=new_name, email=new_email,
                                tel_num=new_telnum, china_id=new_chinaid)
    user_list = UserInfo.objects.all()
    return render(request, 'polls/showdb.html', {'user_list':user_list})
def modifydb(request):
    user_list = UserInfo.objects.all()
    return render(request, 'polls/showdb.html', {'user_list': user_list})


def additem(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            data = form.clean()
            print data
        else:
            error_msg = form.errors
            return render(request,'polls/form_test.html',{'obj':form, 'errors':error_msg})
    return render(request,'polls/form_test.html',{'obj':ItemForm()})
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        if username == 'gml' and pwd == '123456':
            request.session['IS_lOGIN'] = True
            request.session['USRNAME'] = 'gml'
            return redirect(reverse('polls:home',args=[]))
    return render(request,'polls/login.html')
def home(request):
    username = request.session.get('USRNAME','anybody')
    return render(request,'polls/home.html',{'username':username})
def logout(request):
    del request.session['USRNAME']
    return HttpResponse('logout ok!')