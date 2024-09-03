from django.urls import path
from .views import fiverr_keyword_search,keyword_research_and_title

urlpatterns = [
    path('keyword-research-and-title/<str:keyword>/', keyword_research_and_title, name='keyword_research_and_title'),
    path('fiverr-keyword/<str:keyword>/', fiverr_keyword_search, name='fiverr-keyword-search'),
]

