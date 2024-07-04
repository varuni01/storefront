from django.shortcuts import render
from django.utils import timezone
from django.utils.translation import gettext as _
from .models import VisitorCounter

def home_view(request):
    visitor_counter, created = VisitorCounter.objects.get_or_create(id = 1)
    visitor_counter.count += 1
    visitor_counter.save()
    context = {
        'greeting': _("Welcome to our Localization Project!"),
        'large_number': 12345.67,
        'current_date': timezone.now(),
        'redirect_to': request.path,
        'num_visitors' : visitor_counter.count,
    }
    return render(request, 'home.html', context)


