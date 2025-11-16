import requests, os
import pprint

from django.views.generic import TemplateView
from dotenv import load_dotenv

load_dotenv()


pp = pprint.PrettyPrinter()
class IndexPageView(TemplateView):
    template_name = 'main/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        apikey_newsapi = os.getenv("APIKEY_NEWSAPI")
        url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={apikey_newsapi}'
        response = requests.get(url)
        data = response.json()
        articles = data.get('articles', []) if response.status_code == 200 else []

        context['articles'] = articles
        return context

class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'
