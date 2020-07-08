from django.db import models

# News::Title - body - date - resource -img


class NewsPost(models.Model):
    title = models.CharField(max_length=128, unique=True)
    content = models.TextField(default=' ')
    img = models.ImageField(
        upload_to='news/', null=True, blank=True)
    resource = models.CharField(max_length=64, default='', blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ToolsPost(models.Model):
    tools = [('Masks', 'اقنعة'), ('Sterilizers', 'معقمات'),
             ('Gloves', 'كفوف'), ('Recomended', 'الموصى بها')]

    category = models.CharField(max_length=128, choices=tools)
    title = models.CharField(max_length=128, unique=True)
    content = models.TextField(default=' ', blank=True)
    img = models.ImageField(
        upload_to='tools/', null=True, blank=True)

    def __str__(self):
        return self.title


class AwarenessPost(models.Model):
    title = models.CharField(max_length=128, unique=True)
    content = models.TextField(default=' ')
    img = models.ImageField(
        upload_to='awareness/', null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class BePositivePost(models.Model):
    title = models.CharField(max_length=128, unique=True)
    content = models.TextField(default=' ')
    img = models.ImageField(
        upload_to='bePositive/', null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
