from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Title, Implementation, Tactics, Technics, Threat


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
        tactics = Tactics.objects.all().order_by('id')
        threats = Threat.objects.all().order_by('id')
        context = {'tactics': tactics, 'implements': implements, 'threats': threats}
        return render(request, 'index.html', context)

    def post(self, request):
        """получение выбранного списка из чекбоксов и рендер"""
        threat_id = request.POST.get('number_threat')
        #print(threat_number)
        list_of_tactics = request.POST.getlist('list_tactic_id')
        list_of_technics = request.POST.getlist('list_technic_id')
        implement_id = request.POST.get('implement_id')
        # соxранение данных в сессию для дальнейшего построения pdf
        request.session['tactics_session_id'] = list_of_tactics
        request.session['technics_session_id'] = list_of_technics
        request.session['implement_id'] = implement_id
        request.session['threat_number'] = threat_id

        tactics = Tactics.objects.filter(id__in=list_of_tactics)
        technics = Technics.objects.filter(id__in=list_of_technics).order_by('number')
        threat = get_object_or_404(Threat, pk=threat_id)
        # implement = Implementation.objects.get(pk=implement_id)
        implement = get_object_or_404(Implementation, pk=implement_id)
        context = {'tactics': tactics, 'technics': technics, 'implement': implement, 'threat': threat,}
        return render(request, 'result.html', context)


class GeneratePdfView(View):

    def get(self, request):
        """рендеринг pdf сценария через session"""
        # данные из сессии
        list_tactics_id = request.session['tactics_session_id']
        list_technics_id = request.session['technics_session_id']
        implement_id = request.session['implement_id']
        threat_number = request.session['threat_number']
        # print(list_tactics_id)
        tactics = Tactics.objects.filter(id__in=list_tactics_id)
        technics = Technics.objects.filter(id__in=list_technics_id).order_by('number')
        # implement = Implementation.objects.get(pk=implement_id)
        implement = get_object_or_404(Implementation, pk=implement_id)
        threat = get_object_or_404(Threat, pk=threat_number)
        html_string = render_to_string('pdf.html', {'tactics': tactics, 'technics': technics, 'implement': implement, 'threat': threat})
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
#         return respons
