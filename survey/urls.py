from django.urls import path
from .views import survey_view, thank_you

urlpatterns = [
    path('', survey_view, name='survey'),
    path('thank-you/', thank_you, name='thank_you'),
]
