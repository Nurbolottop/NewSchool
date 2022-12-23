from django.shortcuts import render

from apps.parents.models import Parents

from apps.contacts.models import Contact

from apps.settings.models import Settings

# Create your views here.

def parents(request):
    setting = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    faq = Parents.objects.all()
    
    context = {
        'setting':setting,
        'contact':contact,
        'faq':faq,
    }

    return render(request, 'parents.html', context)