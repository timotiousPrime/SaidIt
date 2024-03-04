# Generic Views
from django.views.generic import View
from django.shortcuts import render

# Create your views here.


class LandingPageView(View):
    template_name = "main/landingPage.html"

    def get(self, request):
        return render(request, self.template_name, {})
