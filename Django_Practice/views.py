# I have created this file - Sachin
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'bootstrap1.html')

def about(request):
    return HttpResponse('About hello world...!')

def FutureReadyTalent(request):
    return HttpResponse('<a href="https://futurereadytalent.in/learning"> FutureReadyTalent </a>')

def removepunc(request):
    print(request.POST.get('text', 'default'))
    return HttpResponse('Removing Punctuation')

def analysis(request):
    analysis_text = request.POST.get('text', 'default')
    analysis_option = request.POST.get('analyze', 'off')
    upper_option = request.POST.get('upper', 'off')
    print(analysis_text, analysis_option, upper_option)
    Punctuation = """!@#$%^&*()_-+='"{\|,.<>?/;:~`}[]"""
    analysed = ''
    upper = ''
    status = 'Unsuccesful'
    success = 'danger'
    if analysis_option == 'on':
        for text in analysis_text:
            if text not in Punctuation:
                analysed += text
        analysis_text = analysed
        status = 'Succesful'
        success = 'success'
    if upper_option == 'on':
        for text in analysis_text:
            upper += text.upper()
        analysis_text = upper
        status = 'Succesful'
        success = 'success'
    else: 
        print('Something wents wrong...!')
    param = {'Purpose': 'Analysing Text from user', 'About': 'Sachin Vinayak Dabhade', 'analysed': analysis_text, 'status': status, 'success': success}
    return render(request, 'analysis.html', param)

def capfirst(request):
    return HttpResponse('Capitalizing the text')

def newlineremove(request):
    return HttpResponse('Removing new line')

def spaceremover(request):
    return HttpResponse('Space remover')

def charcount(request):
    return HttpResponse('Coung characters')