from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView
from .models import NewsPost, ToolsPost, AwarenessPost


def HomePageView(request):
    return render(request, "HomePage.html")


class NewsPostView(View):
    def get(self, request):
        News_Posts = NewsPost.objects.all().order_by('-date')
        context = {'NewsPosts': News_Posts}
        return render(request, 'News.html', context)


def StatisticsView(request):
    return render(request, "Statistics.html")


def ContactView(request):
    return render(request, "Contact.html")


# class ToolsPostView(View):
#     model = ToolsPost
#     context_object_name = 'ToolsPosts'
#     template_name = 'Tools.html'

class ToolsPostView(View):
    def get(self, request):
        Tools_Posts = ToolsPost.objects.all()
        context = {'ToolsPosts': Tools_Posts}
        return render(request, 'Tools.html', context)


class AwarenessPostView(View):
    def get(self, request):
        Awareness_Posts = AwarenessPost.objects.all().order_by('-date')
        context = {'AwarenessPost': Awareness_Posts}
        return render(request, 'News.html', context)


# class HomePageView(View):
#     def get(self, request):
#         all_features = CoronaFeature.objects.all()
#         context = {'features': all_features}
#         return render(request, 'HomePage.html', context)
