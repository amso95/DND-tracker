from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Race, NPC, Names, MaleNames, FemaleNames, FamilyNames
from django.core.exceptions import ValidationError
from django.core import serializers

def test(request):
    return render(request, 'npc/base.html')

def home(request):
    order_by = request.GET.get('order_by', 'raceName')
    races = Race.objects.all().order_by(order_by)
    fn = FemaleNames.objects.all()
    mn = MaleNames.objects.all()
    n = Names.objects.all()
    familyN = FamilyNames.objects.all()
    npcForm = NPCFrom(request.POST)
    femaleNames = serializers.serialize('json',fn)
    maleNames = serializers.serialize('json',mn)
    raceJSON = serializers.serialize('json',races)
    noneNames = serializers.serialize('json',n)
    familyNnames = serializers.serialize('json',familyN)

    if request.method == 'POST':
        if npcForm.is_valid():
            for f in fn:
                if(f.femaleName == npcForm.cleaned_data['firstName'] and f.race == npcForm.cleaned_data['race']):
                    FemaleNames.objects.get(femaleName=npcForm.cleaned_data['firstName'], race=npcForm.cleaned_data['race']).delete()
            for m in mn:
                if(m.maleName == npcForm.cleaned_data['firstName'] and m.race == npcForm.cleaned_data['race']):
                    MaleNames.objects.get(maleName=npcForm.cleaned_data['firstName'], race=npcForm.cleaned_data['race']).delete()
            for x in n:
                if(x.name == npcForm.cleaned_data['firstName'] and x.race == npcForm.cleaned_data['race']):
                    Names.objects.get(name=npcForm.cleaned_data['firstName'], race=npcForm.cleaned_data['race']).delete()
            npcForm.save()
            npcForm = NPCFrom()
    return render(request, 'npc/home.html', {'races': races, 'npcForm': npcForm, 'femaleNames': femaleNames, 'maleNames': maleNames, 'raceJSON': raceJSON, 'noneNames': noneNames, 'familyNnames': familyNnames})

def createRace(request):
    raceForm = RaceForm(request.POST)
    if request.method == 'POST':
        if raceForm.is_valid():
            raceForm.save()
            raceForm = RaceForm()
    return render(request, 'npc/createRace.html', {'raceForm': raceForm })

def createName(request):
    nameForm = NamesForm(request.POST)
    if request.method == 'POST':
        if nameForm.is_valid():
            nameForm.save()
            nameForm = NamesForm()
    return render(request, 'npc/createName.html', {'nameForm': nameForm })

def createFemaleName(request):
    femaleNameForm = FemaleNamesForm(request.POST)
    if request.method == 'POST':
        if femaleNameForm.is_valid():
            femaleNameForm.save()
            femaleNameForm = FemaleNamesForm()
    return render(request, 'npc/createFemaleName.html', {'femaleNameForm': femaleNameForm })
    
def createMaleName(request):
    maleNameForm = MaleNamesForm(request.POST)
    if request.method == 'POST':
        if maleNameForm.is_valid():
            maleNameForm.save()
            maleNameForm = MaleNamesForm()
    return render(request, 'npc/createMaleName.html', {'maleNameForm': maleNameForm })
    
def createFamilyName(request):
    familyNameForm = FamilyNamesForm(request.POST)
    if request.method == 'POST':
        if familyNameForm.is_valid():
            familyNameForm.save()
            familyNameForm = FamilyNamesForm()
    return render(request, 'npc/createFamilyName.html', {'familyNameForm': familyNameForm })

def listNPC(request):
    order_by = request.GET.get('order_by', 'firstName')
    npcs = NPC.objects.all().order_by(order_by)
    return render(request, 'npc/listnpc.html', {'npcs': npcs, 'order_by': order_by})

def editNPC(request, pk):
    post = get_object_or_404(NPC,pk=pk)
    if request.method == 'POST':
        npcForm = NPCFrom(request.POST, instance=post)
        if npcForm.is_valid():
            npcForm.save()
            return redirect('/npc/list/npc/')  
    else:
        npcForm = NPCFrom(instance=post)
    return render(request, 'npc/editnpc.html', {'post': post, 'npcForm': npcForm})

def listRace(request):
    order_by = request.GET.get('order_by', 'raceName')
    races = Race.objects.all().order_by(order_by)
    return render(request, 'npc/listRaces.html', {'races': races, 'order_by': order_by})

def editRace(request, pk):
    post = get_object_or_404(Race, pk=pk)
    if request.method == 'POST':
        raceForm = RaceForm(request.POST, instance=post)
        if raceForm.is_valid():
            raceForm.save()
            return redirect('/npc/list/race/')  
    else:
        raceForm = RaceForm(instance=post)
    return render(request, 'npc/editRace.html', {'post': post, 'raceForm': raceForm})

def listName(request):
    order_by = request.GET.get('order_by', 'name')
    names = Names.objects.all().order_by(order_by)
    return render(request, 'npc/listNames.html', {'names': names, 'order_by': order_by})

def editName(request, pk):
    post = get_object_or_404(Names, pk=pk)
    if request.method == 'POST':
        namesForm = NamesForm(request.POST, instance=post)
        if namesForm.is_valid():
            namesForm.save()
            return redirect('/npc/list/name/')  
    else:
        namesForm = NamesForm(instance=post)
    return render(request, 'npc/editName.html', {'post': post, 'namesForm': namesForm})

def listFemaleName(request):
    order_by = request.GET.get('order_by', 'femaleName')
    femaleNames = FemaleNames.objects.all().order_by(order_by)
    return render(request, 'npc/listFemaleNames.html', {'femaleNames': femaleNames, 'order_by': order_by})

def editFemaleName(request, pk):
    post = get_object_or_404(FemaleNames, pk=pk)
    if request.method == 'POST':
        femaleNamesForm = FemaleNamesForm(request.POST, instance=post)
        if femaleNamesForm.is_valid():
            femaleNamesForm.save()
            return redirect('/npc/list/femalename/')  
    else:
        femaleNamesForm = FemaleNamesForm(instance=post)
    return render(request, 'npc/editFemaleName.html', {'post': post, 'femaleNamesForm': femaleNamesForm})

def listMaleName(request):
    order_by = request.GET.get('order_by', 'maleName')
    maleNames = MaleNames.objects.all().order_by(order_by)
    return render(request, 'npc/listMaleNames.html', {'maleNames': maleNames, 'order_by': order_by})

def editMaleName(request, pk):
    post = get_object_or_404(MaleNames, pk=pk)
    if request.method == 'POST':
        maleNamesForm = MaleNamesForm(request.POST, instance=post)
        if maleNamesForm.is_valid():
            maleNamesForm.save()
            return redirect('/npc/list/malename/')  
    else:
        maleNamesForm = MaleNamesForm(instance=post)
    return render(request, 'npc/editMaleName.html', {'post': post, 'maleNamesForm': maleNamesForm})

def listFamilyName(request):
    order_by = request.GET.get('order_by', 'familyName')
    familyNames = FamilyNames.objects.all().order_by(order_by)
    return render(request, 'npc/listFamilyNames.html', {'familyNames': familyNames, 'order_by': order_by})

def editFamilyName(request, pk):
    post = get_object_or_404(FamilyNames, pk=pk)
    if request.method == 'POST':
        familyNamesForm = FamilyNamesForm(request.POST, instance=post)
        if familyNamesForm.is_valid():
            familyNamesForm.save()
            return redirect('/npc/list/familyname/')  
    else:
        familyNamesForm = FamilyNamesForm(instance=post)
    return render(request, 'npc/editFamilyName.html', {'post': post, 'familyNamesForm': familyNamesForm})

def deleteFamilyName(request, pk):
    post = get_object_or_404(FamilyNames, pk=pk)
    if request.method == 'POST':
        post.delete()
    return redirect('/npc/list/familyname/')  
    

def deleteFemaleName(request, pk):
    post = get_object_or_404(FemaleNames, pk=pk)
    if request.method == 'POST':
        post.delete()
    return redirect('/npc/list/femalename/')  

def deleteMaleName(request, pk):
    post = get_object_or_404(MaleNames, pk=pk)
    if request.method == 'POST':
        post.delete()
    return redirect('/npc/list/malename/')  

def deleteName(request, pk):
    post = get_object_or_404(Names, pk=pk)
    if request.method == 'POST':
        post.delete()
    return redirect('/npc/list/name/')  

def deleteNPC(request, pk):
    post = get_object_or_404(NPC, pk=pk)
    if request.method == 'POST':
        post.delete()
    return redirect('/npc/list/npc/')  

def deleteRace(request, pk):
    post = get_object_or_404(Race, pk=pk)
    if request.method == 'POST':
        post.delete()
    return redirect('/npc/list/race/')  


class RaceForm(ModelForm):
    class Meta:
        model = Race
        fields = ['raceName']

class NPCFrom(ModelForm):
    class Meta:
        model = NPC
        fields = ['firstName', 'lastName', 'race', 'aligment', 'city', 'role', 'age', 'comment']

class NamesForm(ModelForm):
    class Meta:
        model = Names
        fields = ['name', 'race']

class MaleNamesForm(ModelForm):
    class Meta:
        model = MaleNames
        fields = ['maleName', 'race']

class FemaleNamesForm(ModelForm):
    class Meta:
        model = FemaleNames
        fields = ['femaleName', 'race']

class FamilyNamesForm(ModelForm):
    class Meta:
        model = FamilyNames
        fields = ['familyName', 'race']