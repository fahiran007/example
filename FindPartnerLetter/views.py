from django.shortcuts import render,redirect
from FindPartnerLetter.models import userinfo
from random import choice
from . import idx_gen

# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        nickname = request.POST.get('nickname')
        birthyear = request.POST.get('birthyear')
        bestfriend = request.POST.get('bestfriend')
        hobby = request.POST.get('hobby')
        li = ['ABCDEFGHIJKLMNOPRSTWZ']
        if userinfo.objects.filter(name=name,Bestfriend=bestfriend,Birthyear=birthyear).first():
            inf = userinfo.objects.get(name=name,nickName=nickname,Birthyear=birthyear,Bestfriend=bestfriend)
            letter = inf.letter
            idx = inf.idx
        else:
            letter = choice(li[0])
            idx = idx_gen.idx_g()
            info = userinfo(name=name,nickName=nickname,Birthyear=birthyear,Bestfriend=bestfriend,Hobby=hobby,letter=letter,idx=idx)
            info.save()
        return redirect('/Result/'+idx)
    return render(request, 'index.html')
def info(request,idx):
    inf = userinfo.objects.get(idx=idx)
    infos = {
            'name':inf.name,
            'nickname':inf.nickName,
            'birthyear':inf.Birthyear,
            'bestfriend':inf.Bestfriend,
            'hobby':inf.Hobby,
            'letter':inf.letter,
            'idx':idx
        }
    datas = userinfo.objects.all()
    return render(request, 'info.html',{'infos':infos,'datas':datas})
    