from django.shortcuts import render
from django.db.models import Q # new

# Create your views here.
from django.views.generic import TemplateView, ListView

from .models import Intity,Region,Classification


class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Intity
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Intity.objects.filter(
            Q(name__icontains=query)| Q(works=query)
        )
        return object_list