from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView
from .models import NewsPost, ToolsPost, AwarenessPost

from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
# from django.contrib.auth import authenticate, login


def HomePageView(request):
    return render(request, "HomePage.html")


def StatisticsView(request):
    return render(request, "Statistics.html")


def ContactView(request):
    return render(request, "Contact.html")


class NewsPostView(View):
    def get(self, request):
        News_Posts = NewsPost.objects.all().order_by('-date')
        pt = 'الاخبار'
        context = {'NewsPosts': News_Posts, 'PT': pt}
        return render(request, 'News.html', context)


class ToolsPostView(View):
    def get(self, request):
        Tools_Posts = ToolsPost.objects.all().order_by('category')
        pt = 'ادوات الوقاية'
        context = {'ToolsPosts': Tools_Posts, 'PT': pt}
        return render(request, 'Tools.html', context)


class AwarenessPostView(View):
    def get(self, request):
        Awareness_Posts = AwarenessPost.objects.all().order_by('-date')
        pt = 'طريق الوقاية'
        context = {'AwarenessPost': Awareness_Posts, 'PT': pt}
        return render(request, 'Awareness.html', context)


def contact_form(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f'Message from {form.cleaned_data["name"]}'
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["email"]
            recipients = ['mustafa.raad.m7@gmail.com']
            try:
                send_mail(subject, message, sender,
                          recipients, fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return HttpResponse('Success...Your email has been sent')
    return render(request, 'Contact.html', {'form': form})
