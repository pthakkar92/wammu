from django.shortcuts import render_to_response, get_object_or_404
from wammu_web.wammu.helpers import WammuContext
from wammu_web.news.models import Entry, Category

# Create your views here.

def entry(request, slug, day = None, month = None, year = None):
    entry = get_object_or_404(Entry, slug = slug)
    return render_to_response('news/entry.html', WammuContext(request, {
        'entry': entry,
    }))

def category(request, slug):
    return ''
