import json  # 파이썬 기본에서 지원
from django.http import HttpResponse
from django.shortcuts import render
from .models import Professor


def professor_list(request):
    qs = Professor.objects.all()  # DB에서 모든 Professor 목록을 가져올 준비.

    query = request.GET.get('query', '')
    if query:
        qs = qs.filter(name__icontains=query)

    return render(request, 'univ/professor_list.html', {
        'professor_list': qs,
    })


def professor_list_json(request):
    qs = Professor.objects.all()

    query = request.GET.get('query', '')
    if query:
        qs = qs.filter(name__icontains=query)

    professor_list = [
        professor.as_dict()
        for professor in qs]  # list comprehension
    json_string = json.dumps(professor_list, ensure_ascii=False)
    return HttpResponse(json_string)
