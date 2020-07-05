from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
    _text = {'res':''}
    if request.method == 'POST':
        try:
            initial = request.POST.get('initial').split('-')
            final = request.POST.get('final').split('-')

            ini = datetime.date(*tuple(map(int,initial))) 
            fin = datetime.date(*tuple(map(int,final)))
            diff = fin-ini
            text = f"It has been {diff.days} day(s)"
            _text['res'] = text
        except:
            return render(request,'index.html',{'result':'You cannot leave fields blank!'})
    return render(request,'index.html',{'result':_text['res']})