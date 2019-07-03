from django.shortcuts import render
from .forms.form import SubjectForm
# Create your views here.


def eligability(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

        else:
            form = SubjectForm()