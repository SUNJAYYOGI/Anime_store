
from django.shortcuts import render, get_object_or_404
from .models import Anime

def home(request):
    animes = Anime.objects.all()
    return render(request, 'home.html', {'animes': animes})

def anime_detail(request, anime_id):
    anime = get_object_or_404(Anime, id=anime_id)
    return render(request, 'anime_detail.html', {'anime': anime})

def about(request):
    return render(request, 'about.html')

def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Anime.objects.filter(title__icontains=query)
    return render(request, 'search.html', {'query': query, 'results': results})
