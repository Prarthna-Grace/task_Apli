from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import AllLevels


def test(request):
    ac=AllLevels.objects.all()
    template=loader.get_template('Jumpstart/Level.html')
    context={
      'ac':ac,
    }
    return HttpResponse(template.render(context,request))

def detail(request, test_id):
    test=get_object_or_404(AllLevels, pk=test_id)
    return render(request, 'Jumpstart/detail.html' )


def yourchoice(request, test_id):
    test=get_object_or_404(AllLevels, pk=test_id)
    try:
        selected_ct=test.details_set.get(pk=request.POST('choice'))
    except (KeyError,AllLevels.DoesNotExist):
        return render(request,'Jumpstart/detail.html',{
            'test':test,
            'error_message':"Select a valid option",
        })
    else:
        selected_ct.your_choice=True
        selected_ct.save()
        return render(request,'Jumpstart/detail.html',{'test':test})

