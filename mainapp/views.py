from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Title, Implementation, Tactics, Technics


from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint


class TacticsView(View):
    """
    Все тактики
    """

    def get(self, request):
        implements = Implementation.objects.all()
        tactics = Tactics.objects.all()
        context = {'tactics': tactics, 'implements': implements}
        return render(request, 'index.html', context)

    def post(self, request):
        """получение выбранного списка из чекбоксов и рендер"""
        list_of_tactics = request.POST.getlist('list_tactic_id')
        list_of_technics = request.POST.getlist('list_technic_id')
        implement_id = request.POST.get('implement_id')
        # соxранение данных в сессию для дальнейшего построения pdf
        request.session['tactics_session_id'] = list_of_tactics
        request.session['technics_session_id'] = list_of_technics
        request.session['implement_id'] = implement_id

        tactics = Tactics.objects.filter(id__in=list_of_tactics)
        technics = Technics.objects.filter(id__in=list_of_technics)
        implement = Implementation.objects.get(pk=implement_id)
        context = {'tactics': tactics, 'technics': technics, 'implement': implement}
        return render(request, 'result.html', context)


class GeneratePdfView(View):

    def get(self, request):
        """рендеринг pdf сценария через session"""
        # данные из сессии
        list_tactics_id = request.session['tactics_session_id']
        list_technics_id = request.session['technics_session_id']
        implement_id = request.session['implement_id']
        # print(list_tactics_id)
        tactics = Tactics.objects.filter(id__in=list_tactics_id)
        technics = Technics.objects.filter(id__in=list_technics_id)
        implement = Implementation.objects.get(pk=implement_id)
        html_string = render_to_string('pdf.html', {'tactics': tactics, 'technics': technics, 'implement': implement})
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="tactics.pdf"'
        weasyprint.HTML(string=html_string).write_pdf(response,
                                                      stylesheets=[weasyprint.CSS('static/css/pdf.css')])
        return response


# class GeneratePdfView(View):
#     def post(self, request):
#         """рендеринг pdf сценария через передачу переменной из шаблона"""
#         # list_of_tactics = request.POST.getlist('list_tactics')
#         list_of_tactics = request.POST.getlist('list_tactics')
#         # print(dir(request.POST))
#         print(list_of_tactics)
#         # list_of_technics = request.POST.getlist('list_technic_id')
#         tactics = Tactics.objects.filter(id__in=list_of_tactics)
#
#         # technics = Technics.objects.filter(id__in=list_of_technics)
#         html_string = render_to_string('pdf.html', {'tactics': tactics, })
#         response = HttpResponse(content_type='application/pdf')
#         response['Content-Disposition'] = 'filename="tactics.pdf"'
#         weasyprint.HTML(string=html_string).write_pdf(response,
#                                                       stylesheets=[weasyprint.CSS('static/css/pdf.css')])
#         return response