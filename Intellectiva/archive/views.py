from django.shortcuts import render
from .models import Paper

# Create your views here.


def archive(request):
    allPapers = Paper.objects.all()
    return render(request, "archive.html", {"allPapers": allPapers})


def rPaper(request, slug):
    paper = Paper.objects.filter(slug=slug).first()
    return render(request, "rpaper.html", {"paper": paper})
