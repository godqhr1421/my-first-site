from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#elections/view.py 열어서 수정하기
from .models import Candidate #models에 정의된 Candidate를 import


def index(request):

    candidates = Candidate.objects.all() #Candidate에 있는 모든 객체를 불러옵니다
    context = {'candidates' : candidates}
    return render(request, 'elections/index.html',context)
