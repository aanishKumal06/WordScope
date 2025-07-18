from django.urls import path
from .views import HomePage, TextAnalysisView, TextStatsView, WordFrequencyView

urlpatterns = [
    path('text-stats/', TextStatsView.as_view(), name='text_stats'), 
    path('word-frequency/', WordFrequencyView.as_view(), name='word_frequency'), 
    path('text-analysis/', TextAnalysisView.as_view(), name='text_analysis'),
    path('', HomePage.as_view(), name='home'),
]