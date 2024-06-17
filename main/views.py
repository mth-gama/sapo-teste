import requests
import pprint

from django.views.generic import TemplateView



pp = pprint.PrettyPrinter()
class IndexPageView(TemplateView):
    template_name = 'main/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=c75ad3b91cbb490daeea9bae96348f2f'
        response = requests.get(url)
        data = response.json()
        articles = data.get('articles', []) if response.status_code == 200 else []

        context['articles'] = articles
        return context

class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'
