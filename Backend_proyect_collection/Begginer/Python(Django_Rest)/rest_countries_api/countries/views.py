from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from bs4 import BeautifulSoup
from .models import CountriesModel
from .serializers import CountriesSerializer

class ScrapeCountriesView(APIView):
    def get(self, request):
        url = "https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses"
        headers = {
            'User-Agent': 'MiScraper/1.0 (+https://tu-web-o-email-contacto.com)'
        }
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find('table', class_='wikitable sortable col1cen')

            if not table:
                return Response({"error": "Table not found"}, status=status.HTTP_404_NOT_FOUND)

            # Cleaning current table
            CountriesModel.objects.all().delete()

            rows = table.find_all('tr')
            
            for row in rows[1:]:
                cols = row.find_all(['td', 'th'])
                if len(cols) < 6: 
                    continue  # ignore incomplete rows

                img_tag = cols[0].find('img')
                img_url = 'https:' + img_tag['src'] if img_tag and img_tag.has_attr('src') else ''

                completed_name = cols[1].text.strip()
                sovereignty = cols[5].text.strip()
                capital = cols[2].text.strip()
                continent = cols[3].text.strip()

                CountriesModel.objects.create(
                    img=img_url,
                    completed_name=completed_name,
                    sovereignty=sovereignty,
                    capital=capital,
                    continent=continent,
                )

            countries = CountriesModel.objects.all()
            serializer = CountriesSerializer(countries, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



