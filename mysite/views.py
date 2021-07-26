"""from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>This is the best website to learn python.<a href ='https://www.javatpoint.com/python-tutorial'>javatpoint</a></h1>"
                        "<h2>Learn python for beginner.  <a href='https://www.w3schools.com/python/'>W3schoool.com</a></h2>")

def about(request):
    return HttpResponse("This is about page")"""
from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request,'index2.html')


def analyze(request):
    #Get the text
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    print(djtext)
    print(removepunc)
    # analyzed = djtext
    if removepunc == "on":
        punctuation = '''<>.,/?;:!@#$%^&*()_'=[]{}|`~,_'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed+char

        param = {'purpose':'Remove Punctuation','analyze_text':analyzed}
        djtext =analyzed
        # return render(request,'analyze2.html',param)
    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        param = {'purpose': 'Change to upper case', 'analyze_text': analyzed}
        djtext =analyzed
        # return render(request, 'analyze2.html', param)
    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        param = {'purpose': 'New line', 'analyze_text': analyzed}
        djtext =analyzed
        # return render(request,'analyze2.html',param)
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):


                analyzed = analyzed + char
        param = {'purpose': 'Extra Space remove', 'analyze_text': analyzed}
        djtext =analyzed
    if (removepunc != "on" and fullcaps != "on" and extraspaceremover !="on" and newlineremover!= "on"):
        return HttpResponse('Error! Please select any of the operation.')

    return render(request, 'analyze2.html', param)








