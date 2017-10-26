from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class BlogView(View):
    def get(self, request):
        return

    def post(self, request):
        return

    def delete(self, request):
        return

    def put(self, request):
        return

def blog_list(request):
    return

def form(request, pk):
    return