from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Title, Implementation, Tactics, Technics


class TacticsView(View):
    """
    Все тактики
    """
    def get(self, request):
        tactics = Tactics.objects.all()
        context = {'tactics': tactics}
        return render(request, 'index.html', context)

    def post(self, request):
        """получение выбранного списка из чекбоксов и рендер"""
        list_of_tactics = request.POST.getlist('filetouse')
        list_of_technics = request.POST.getlist('filetouse2')
        # print(list_of_tactics)
        # print(list_of_technics)
        tactics = Tactics.objects.filter(id__in=list_of_tactics)
        technics = Technics.objects.filter(id__in=list_of_technics)
        # не работает итерация в шаблоне
        numbers = []
        for i in range(1,11):
            numbers.append(i)
        context = {'tactics': tactics, 'technics': technics, 'numbers': numbers}
        return render(request, 'result.html', context)

