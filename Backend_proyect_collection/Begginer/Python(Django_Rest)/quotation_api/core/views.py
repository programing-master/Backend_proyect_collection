from rest_framework.decorators import api_view
from rest_framework.response import Response
from bs4 import BeautifulSoup
import pandas as pd
import requests
import random


class QuoteAPI:
    results = []

    @api_view(['GET'])
    def quote(request):
        #get url and fetch data
        url = "https://quotes.toscrape.com/"
        response = requests.get(url)

        if response.status_code != 200:
            return Response({"msg": f"Error :{response.status_code}"})

        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")

        QuoteAPI.results.clear()

        for quote in quotes:
            text = quote.find("span", class_="text").get_text()
            author = quote.find("small", class_="author").get_text()
            QuoteAPI.results.append({"quote": text, "author": author})
            
            df = pd.DataFrame(QuoteAPI.results)
            df.to_csv("Quotes.csv", index=False)
        return Response({"quote":random.choice(QuoteAPI.results),"msg": "Quotes exported to Quotes.csv"})
