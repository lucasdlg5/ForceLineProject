from django.shortcuts import render
from django.utils import timezone
from .models import Post

index_view = never_cache(TemplateView.as_view(template_name='index.html'))