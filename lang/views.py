from django.shortcuts import render
from django.utils import timezone
from django.utils.translation import gettext as _
from .models import VisitorCounter
from django.http import HttpResponse
from django.http import JsonResponse
from .utils import read_html_from_file, mark_text_for_translation, save_html_to_file
from .translate_es_po import translate_po_file
from .translate_fr_po import translate_po_file

import os
import logging


def home_view(request):
    visitor_counter, created = VisitorCounter.objects.get_or_create(id=1)
    visitor_counter.count += 1
    visitor_counter.save()
    context = {
        'greeting': _("Welcome to our Localization Project!"),
        'large_number': 12345.67,
        'current_date': timezone.now(),
        'redirect_to': request.path,
        'num_visitors': visitor_counter.count,
    }
    return render(request, 'home.html', context)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def mark_for_translation_view(request):
    file_path = os.path.join(os.path.dirname(__file__), 'templates', 'home.html')

    try:
        html_content = read_html_from_file(file_path)
        marked_html = mark_text_for_translation(html_content)
        save_html_to_file(file_path, marked_html)
        print("Original HTML:")
        print(html_content)
        print("Marked HTML:")
        print(marked_html)

        return HttpResponse("HTML file has been processed and saved with translation tags.")
    except Exception as e:
        print(f"Error: {e}")
        return HttpResponse(f"Error: {e}", status=500)
    
def translate_po_view(request):
    po_file_path = 'locale/es/LC_MESSAGES/django.po' 
    target_language = 'es'  
    try:
        translate_po_file(po_file_path, target_language)
        return HttpResponse("PO file has been translated and updated successfully.")
    except Exception as e:
        return HttpResponse(f"Error during translation: {e}", status=500)

def trigger_translation_view(request):
    po_file_path = 'locale/fr/LC_MESSAGES/django.po'
    translate_po_file(po_file_path, 'fr')
    return HttpResponse("French translation process completed.")



    

