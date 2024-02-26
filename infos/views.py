from django.shortcuts import render
from django.template import Context

def home(request):
    context = Context({'title': 'Strona główna', 'content': 'Witaj na mojej stronie głównej!'})
    return render(request, 'infos/home.html', context)

def about_me(request):
    context = Context({'title': 'O mnie', 'content': 'Krótka informacja o mnie. Plus za zdjęcie.'})
    return render(request, 'infos/about_me.html', context)

def contact(request):
    context = Context({'title': 'Kontakt', 'content': 'Jakieś dane kontaktowe. Plus za formularz, w którym można wpisać treść i wysłać przyciskiem.'})
    return render(request, 'infos/contact.html', context)
