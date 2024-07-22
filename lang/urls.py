from django.urls import path
from . views import home_view
from .views import mark_for_translation_view
from .views import translate_po_view
from .views import trigger_translation_view


urlpatterns = [
    path('', home_view, name='home'),
    path('mark-for-translation/', mark_for_translation_view, name='mark_for_translation'),
    path('translate-po/', translate_po_view, name='translate_po'),
    path('translate-po-fr/', trigger_translation_view, name='trigger_translation'),
]

