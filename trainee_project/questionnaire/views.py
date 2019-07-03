from django.shortcuts import render,redirect
from .forms.form import SubjectForm
from .models import Subject
# Create your views here.


def eligability(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            """
            age = post['age'].value()
            if Subject.is_minor(age):
                return render(request,'participant.html', {'age': age})
            """
            post.save()
            return redirect('eligability')
    else:
        form = SubjectForm()
    return render(request, 'participant.html', {'form': form})