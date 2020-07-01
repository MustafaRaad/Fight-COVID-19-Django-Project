from django.contrib import admin
from .models import  NewsPost, ToolsPost, AwarenessPost, BePositivePost, Contact
# Register your models here.
admin.site.register(NewsPost)
admin.site.register(ToolsPost)
admin.site.register(AwarenessPost)
admin.site.register(BePositivePost)
admin.site.register(Contact)
