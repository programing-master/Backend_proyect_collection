from django.urls import path
from .views import ScrapeCountriesView

urlpatterns = [
    path('scrape-countries/', ScrapeCountriesView.as_view(), name='scrape-countries'),

]