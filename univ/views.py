from django.shortcuts import render
from .models import Professor


def professor_list(request):
    qs = Professor.objects.all()  # DB에서 모든 Professor 목록을 가져올 준비.
    return render(request, 'univ/professor_list.html', {
        'professor_list': qs,
    })
